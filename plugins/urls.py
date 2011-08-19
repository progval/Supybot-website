from django.conf.urls.defaults import patterns, include, url

from plugins import feeds

charClass = '[a-zA-Z0-9]+'

urlpatterns = patterns('website.plugins.views',
    url(r'^$',                             'index', name='plugins_index'),
    url(r'^page/(?P<page>[0-9]+)/$',       'listing', name='plugins_listing'),
    url(r'^view/(?P<name>%s)/$'% charClass,'view', name='plugins_view'),
    url(r'^admin/$',                       'admin_index', name='plugins_admin_index'),
    url(r'^admin/(?P<name>%s)/$'%charClass,'admin_form', name='plugins_admin_form'),
    url(r'^submit/$',                      'submit', name='plugins_submit'),

    (r'^feeds/rss/updates/$',              feeds.LatestPluginUpdatesRssFeed()),
    (r'^feeds/atom/updates/$',             feeds.LatestPluginUpdatesAtomFeed()),
)

