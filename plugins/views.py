import datetime
import os
import re

from django.contrib.auth.decorators import login_required
from django.core.exceptions import SuspiciousOperation
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.forms import ModelForm
from django.http import Http404
from django.http import HttpResponseForbidden

from voting.models import Vote

from plugins.models import Plugin, PluginSubmitForm, PluginEditForm
from plugins.models import GitRepository, GitRepositoryForm
from plugins.models import PluginComment
from plugins import daemons

from settings import MEDIA_ROOT

plugin_matcher = re.compile('[A-Z][A-Za-z0-9]+')

def index(request):
    return redirect(listing, 1)

def listing(request, page):
    plugins = Plugin.objects.filter(published=True)
    paginator = Paginator(list(plugins), 100)
    try:
        plugins = paginator.page(page)
    except:
        raise Http404()
    plugins = plugins.object_list
    ratings = Vote.objects.get_scores_in_bulk(plugins)
    for plugin in plugins:
        try:
            pluginData = ratings[plugin]
        except KeyError:
            pluginData = {'score': 0, 'num_vote': 0}
        plugin.score = pluginData['score']
        plugin.num_vote = pluginData['num_vote']
    context = {'plugins': plugins}
    return render_to_response('plugins/listing.tpl', context)

class PluginCommentForm(ModelForm):
    class Meta:
        model = PluginComment
        fields = ('text',)

@csrf_protect
def view(request, name):
    plugin = get_object_or_404(Plugin, name=name, published=True)
    if request.method == 'POST' and request.user.is_authenticated():
        if '-1' in request.POST:
            Vote.objects.record_vote(plugin, request.user, -1)
        elif '0' in request.POST:
            Vote.objects.record_vote(plugin, request.user, 0)
        elif '+1' in request.POST:
            Vote.objects.record_vote(plugin, request.user, +1)
        else:
            form = PluginCommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.key = plugin
                comment.user = request.user
                comment.save()
    myVote = Vote.objects.get_for_user(plugin, request.user)
    context = Vote.objects.get_score(plugin)
    # Fetch the comments after posting this one.
    comments = PluginComment.objects.filter(key=plugin)

    context.update({'plugin': plugin, 'myvote': myVote, 'user': request.user,
        'comments': comments})
    context.update(csrf(request))
    return render_to_response('plugins/view.tpl', context)

@login_required
def admin_index(request):
    plugins = Plugin.objects.filter(author=request.user)
    context = {'plugins': plugins}
    return render_to_response('plugins/admin_index.tpl', context)

@login_required
@csrf_protect
def admin_form(request, name):
    saved = False
    plugin = get_object_or_404(Plugin, name=name)
    form = None
    if request.method == "POST" and plugin.author == request.user:
        form = PluginEditForm(request.POST, instance=plugin)
        if form.is_valid():
            form.save()
            return redirect(admin_index)
    if form is None:
        form = PluginEditForm(instance=plugin)
    context = {'form': form, 'saved': saved, 'plugin': plugin}
    context.update(csrf(request))
    return render_to_response('plugins/admin_form.tpl', context)

@login_required
@csrf_protect
def submit(request):
    form = None
    if request.method == "POST":
        form = PluginSubmitForm(request.POST)
        if form.is_valid():
            plugin = form.save(commit=False)
            plugin.author = request.user
            form.save()
            return redirect(admin_index)
    if form is None:
        form = PluginSubmitForm()
    context = {'form': form, 'saved': False}
    context.update(csrf(request))
    return render_to_response('plugins/admin_form.tpl', context)

# Threads in which "git clone" is running.
clone_threads = {}

repo_name_matcher = re.compile('[A-Za-z0-9_-]+')

@login_required
@csrf_protect
def autoimport_index(request):
    form = None
    if request.method == "POST":
        form = GitRepositoryForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['url'].startswith('git://'):
                repo = form.save(commit=False)
                repo.maintainer = request.user
                repo.state = 'c'
                form.save()
                thread = daemons.clone(repo)
                clone_threads[repo.name] = (repo, thread)
                return redirect(autoimport_index)
            else:
                form._errors.update({'url': ('This field must start with git://.',)})
    for name, data in clone_threads.items():
        repo, thread = data
        if repo.state == 'c' and not thread.is_alive():
            repo.state = 'n'
            repo.save()
    if form is None:
        form = GitRepositoryForm()
    repositories = list(GitRepository.objects.filter(maintainer=request.user))
    for repo in repositories:
        if repo.name not in clone_threads and repo.state == 'c':
            repo.state = 'n'
            repo.save()
    context = {'form': form, 'repositories': repositories}
    context.update(csrf(request))
    return render_to_response('plugins/autoimport/index.tpl', context)

@login_required
@csrf_protect
def autoimport_repo(request, name):
    repo = get_object_or_404(GitRepository, name=name)
    path = os.path.join(MEDIA_ROOT, 'repositories', '%s' % repo.name)
    if request.method == "POST":
        checkbox_prefix = 'import_plugin_'
        plugins = []
        for name, value in request.POST.items():
            if not name.startswith(checkbox_prefix):
                continue
            assert plugin_matcher.match(name[len(checkbox_prefix):])
            name = name[len(checkbox_prefix):]
            try:
                Plugin.objects.filter(name=name).get()
                errors.append('Plugin %s already exists in the database.')
                continue
            except ObjectDoesNotExist:
                pass
            plugin_path = os.path.join(path, name)
            try:
                readme = open(os.path.join(plugin_path, 'README.txt'), 'r').read()
            except IOError:
                try:
                    readme = open(os.path.join(plugin_path, 'README'), 'r').read()
                except:
                    readme = 'This plugin has no description.'
            plugin = Plugin(
                    author=request.user,
                    name=name,
                    short_description=readme[0:511].split('\n\n')[0],
                    description=readme,
                    git_repo=repo.url)
            plugins.append(plugin)
        # If everything was fine
        for plugin in plugins:
            plugin.save()
        return redirect('plugins_admin_index')

    else:
        timedelta = datetime.datetime.now() - repo.latest_fetch
        if timedelta.days * 86400 + timedelta.seconds > 3600:
            os.system('cd %s && git pull' % path)
            repo.latest_fetch = datetime.datetime.now()
            repo.save()
        raw_list = os.listdir(path)
        raw_list.sort()
        plugins = []
        class Container:
            pass
        for item in raw_list:
            if os.path.isfile(os.path.join(path, item)) or not plugin_matcher.match(item):
                continue
            plugin = Container()
            plugin.name = item
            try:
                plugin.in_database = Plugin.objects.filter(name=item).get()
            except ObjectDoesNotExist:
                pass
            plugins.append(plugin)
        context = {'user': request.user, 'repository': repo, 'plugins': plugins}
        context.update(csrf(request))
        return render_to_response('plugins/autoimport/list.tpl', context)


@login_required
@csrf_protect
def autoimport_delrepo(request, name):
    repo = get_object_or_404(GitRepository, name=name)
    if request.user != repo.maintainer:
        return HttpResponseForbidden()
    assert '.' not in name
    assert '/' not in name
    assert os.system('rm -Rf %s' % os.path.join(MEDIA_ROOT, 'repositories',
        name)) == 0
    repo.delete()
    return redirect(autoimport_index)
