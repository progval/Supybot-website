from django.conf.urls.defaults import patterns, url
from django.conf import settings

urlpatterns = patterns('dpaste.views',
    url(r'^$', 'snippet_new', name='dpaste_snippet_new'),
    url(r'^guess/$', 'guess_lexer', name='dpaste_snippet_guess_lexer'),
    url(r'^diff/$', 'snippet_diff', name='dpaste_snippet_diff'),
    url(r'^your-latest/$', 'snippet_userlist', name='dpaste_snippet_userlist'),
    url(r'^your-settings/$', 'userprefs', name='dpaste_snippet_userprefs'),
    url(r'^(?P<snippet_id>[a-zA-Z0-9]{4})/$', 'snippet_details', name='dpaste_snippet_details'),
    url(r'^(?P<snippet_id>[a-zA-Z0-9]{4})/delete/$', 'snippet_delete', name='dpaste_snippet_delete'),
    url(r'^(?P<snippet_id>[a-zA-Z0-9]{4})/raw/$', 'snippet_details', {'template_name': 'dpaste/snippet_details_raw.html', 'is_raw': True}, name='dpaste_snippet_details_raw'),
)
