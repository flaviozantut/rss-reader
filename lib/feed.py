# -*- coding: utf-8 -*-
"""
    Feed
    ~~~~~~~~~~~~~~~~~~
"""
import feedparser





class Feed:
    """
       Leitura de feeds
    """
    url = None


    def __init__(self, url):
        self.url = url
        self.feedData = feedparser.parse(self.url)


    def entries(self):

        return self.feedData.entries

    def title(self):
        return self.feedData.feed.title