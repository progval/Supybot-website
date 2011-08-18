from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('website.plugins.views',
    url(r'^$',                             'index', name='plugins_index'),
    url(r'^page/(?P<page>[0-9]+)/$',       'listing', name='plugins_listing'),
    url(r'^view/(?P<name>[a-zA-Z0-9]+)/$', 'view', name='plugins_view'),
)

