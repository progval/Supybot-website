from django.conf.urls import patterns, include, url


urlpatterns = patterns('website.get.views',
    url(r'^$',                       'index', name='get_index'),
)

