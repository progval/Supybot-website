from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.http import Http404

from news.models import News

def index(request):
    return redirect(listing, 1)

def listing(request, page):
    newsList = News.objects.filter(published=True)
    paginator = Paginator(list(newsList), 20)
    try:
        newsList = paginator.page(page)
    except:
        raise Http404()
    context = {'page': newsList}
    return render_to_response('news/listing.tpl', context)

def read(request, slug):
    news = get_object_or_404(News, slug=slug)
    context = {'news': news}
    return render_to_response('news/read.tpl', context)
