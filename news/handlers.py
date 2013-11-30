from django.conf.urls import patterns, include, url

from piston.handler import AnonymousBaseHandler, BaseHandler
from piston.resource import Resource

from models import News, NewsComment

class NewsHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = News

    def read(self, request, slug=None):
        if slug is None:
            return News.objects.filter(published=True)
        else:
            return News.objects.get(slug=slug, published=True)

class NewsCommentHandler(BaseHandler):
    allowed_methodes = ('GET',)
    model = NewsComment
    fields = ('text', 'user', ('key', ('slug',)), 'created_date')
    def read(self, request, slug=None):
        news = News.objects.get(slug=slug, published=True)
        return NewsComment.objects.filter(key=news)

news_handler = Resource(NewsHandler)
news_comment_handler = Resource(NewsCommentHandler)
urlpatterns = patterns('',
    url(r'list/', news_handler),
    url(r'read/(?P<slug>.*)/', news_handler),
    url('comments/(?P<slug>.*)/', news_comment_handler)
)
