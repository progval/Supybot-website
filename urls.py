from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',          'website.root.views.home', name='root_home'),
    url(r'^news/',      include('website.news.urls')),
    url(r'^doc/',       include('website.doc.urls')),
    url(r'^get/',       include('website.get.urls')),
    url(r'^plugins/',   include('website.plugins.urls')),
    url(r'^user/',      include('website.users.urls')),
    url(r'^paste/',     include('website.dpaste.urls')),
    url(r'^about/$',    'website.root.views.about', name='root_about'),

    url(r'^api/news/',   include('website.news.handlers')),
    url(r'^api/plugins/',include('website.plugins.handlers')),

    url(r'^search/', include('haystack.urls')),
)
