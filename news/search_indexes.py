import datetime

from haystack.indexes import *
from haystack import site

from news.models import News

class NewsIndex(RealTimeSearchIndex):
    text = CharField(document=True, use_template=True)
    author = CharField(model_attr='author')
    created_at = DateTimeField(model_attr='created_at')
    short_description = CharField(model_attr='short_description')

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return News.objects.filter(created_at__lte=datetime.datetime.now(),
                published=True)

site.register(News, NewsIndex)
