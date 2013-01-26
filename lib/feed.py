# -*- coding: utf-8 -*-
"""
    Feed lib
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
        """
           Recupera as noticias do feed
        """
        return self.feedData.entries

    def title(self):
        """
           Recupera o título do feed
        """
        return self.feedData.feed.title