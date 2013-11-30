from django.conf.urls import patterns, include, url


urlpatterns = patterns('website.users.views',
    url(r'^$',          'index', name='users_index'),
    url(r'^login/$',    'login', name='users_login'),
    url(r'^logout/$',    'logout', name='users_logout'),
    url(r'^register/$',  'register', name='users_register'),
)

