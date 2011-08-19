from django.contrib.syndication.views import Feed
from news.models import News
from django.utils.feedgenerator import Atom1Feed

class LatestNewsUpdatesRssFeed(Feed):
    title = 'Latest Supybot news'
    link = '/news/'
    description = 'Latest news at Supybot website.'

    def items(self):
        return News.objects.order_by('-updated_at')[:10]

class LatestNewsUpdatesAtomFeed(LatestNewsUpdatesRssFeed):
    feed_type = Atom1Feed
    subtitle = LatestNewsUpdatesRssFeed.description

