from django.conf.urls import patterns, include, url

from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',          'root.views.home', name='root_home'),
    url(r'^news/',      include('news.urls')),
    url(r'^get/',       include('get.urls')),
    url(r'^plugins/',   include('plugins.urls')),
    url(r'^user/',      include('users.urls')),
    url(r'^paste/',     include('dpaste.urls')),
    url(r'^about/$',    'root.views.about', name='root_about'),

    url(r'^api/news/',   include('news.handlers')),
    url(r'^api/plugins/',include('plugins.handlers')),
)
