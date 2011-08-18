from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('website.news.views',
    url(r'^$',                       'index', name='news_index'),
    url(r'^page/(?P<page>[0-9]+)/$', 'listing', name='news_listing'),
    url(r'^read/(?P<slug>.*)/$',     'read', name='news_read'),
)

