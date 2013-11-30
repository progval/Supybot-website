from django.conf.urls import patterns, include, url

from news import feeds


urlpatterns = patterns('website.news.views',
    url(r'^$',                       'index', name='news_index'),
    url(r'^page/(?P<page>[0-9]+)/$', 'listing', name='news_listing'),
    url(r'^read/(?P<slug>.*)/$',     'read', name='news_read'),

    (r'^feeds/rss/updates/$',              feeds.LatestNewsUpdatesRssFeed()),
    (r'^feeds/atom/updates/$',             feeds.LatestNewsUpdatesAtomFeed()),
)

