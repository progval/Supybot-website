from django.contrib.auth.decorators import login_required
from django.core.exceptions import SuspiciousOperation
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.http import Http404

from voting.models import Vote

from plugins.models import Plugin, PluginSubmitForm, PluginEditForm

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

@csrf_protect
def view(request, name):
    plugin = get_object_or_404(Plugin, name=name)
    if request.method == 'POST' and request.user.is_authenticated():
        if '-1' in request.POST:
            Vote.objects.record_vote(plugin, request.user, -1)
        elif '0' in request.POST:
            Vote.objects.record_vote(plugin, request.user, 0)
        elif '+1' in request.POST:
            Vote.objects.record_vote(plugin, request.user, +1)
        else:
            raise SuspiciousOperation('Vote is not -1, 0, or +1.')
    myVote = Vote.objects.get_for_user(plugin, request.user)
    context = Vote.objects.get_score(plugin)
    context.update({'plugin': plugin, 'myvote': myVote, 'user': request.user})
    context.update(csrf(request))
    return render_to_response('plugins/view.tpl', context)

@login_required
def admin_index(request):
    plugins = Plugin.objects.filter(author=request.user)
    context = {'plugins': plugins}
    return render_to_response('plugins/admin_index.tpl', context)

@login_required
def admin_form(request, name):
    saved = False
    plugin = get_object_or_404(Plugin, name=name)
    form = None
    if request.method == "POST" and plugin.author == request.user:
        form = PluginEditForm(request.POST, instance=plugin)
        if form.is_valid():
            form.save()
            saved = True
    if form is None:
        form = PluginEditForm(instance=plugin)
    context = {'form': form, 'saved': saved, 'plugin': plugin}
    context.update(csrf(request))
    return render_to_response('plugins/admin_form.tpl', context)

@login_required
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


