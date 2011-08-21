from django.conf.urls.defaults import patterns, include, url

from piston.handler import AnonymousBaseHandler, BaseHandler
from piston.resource import Resource

from models import Plugin, PluginComment

class PluginHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Plugin

    def read(self, request, name=None):
        if name is None:
            return Plugin.objects.filter(published=True)
        else:
            return Plugin.objects.get(name=name, published=True)

class PluginCommentHandler(BaseHandler):
    allowed_methodes = ('GET',)
    model = PluginComment

    fields = ('text', 'user', ('key', ('name',)), 'created_date')

    def read(self, request, name=None):
        plugin = Plugin.objects.get(name=name, published=True)
        return PluginComment.objects.filter(key=plugin)

plugin_handler = Resource(PluginHandler)
plugin_comment_handler = Resource(PluginCommentHandler)
urlpatterns = patterns('',
    url(r'list/', plugin_handler),
    url(r'view/(?P<name>.*)/', plugin_handler),
    url('comments/(?P<name>.*)/', plugin_comment_handler)
)
