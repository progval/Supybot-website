from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.http import Http404

from plugins.models import Plugin

def index(request):
    return redirect(listing, 1)

def listing(request, page):
    plugins = Plugin.objects.filter(published=True)
    paginator = Paginator(list(plugins), 100)
    try:
        plugins = paginator.page(page)
    except:
        raise Http404()
    context = {'page': plugins}
    return render_to_response('plugins/listing.tpl', context)

def view(request, name):
    plugin = get_object_or_404(Plugin, name=name)
    context = {'plugin': plugin}
    return render_to_response('plugins/view.tpl', context)
