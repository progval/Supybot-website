from django.contrib.syndication.views import Feed
from plugins.models import Plugin
from django.utils.feedgenerator import Atom1Feed

class LatestPluginUpdatesRssFeed(Feed):
    title = 'Latest Supybot plugin updates'
    link = '/plugins/'
    description = 'Latest updates of plugins at Supybot website.'

    def items(self):
        return Plugin.objects.order_by('-updated_at')[:10]

class LatestPluginUpdatesAtomFeed(LatestPluginUpdatesRssFeed):
    feed_type = Atom1Feed
    subtitle = LatestPluginUpdatesRssFeed.description
