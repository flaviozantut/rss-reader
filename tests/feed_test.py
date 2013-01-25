# -*- coding: utf-8 -*-
"""
    Feed test
    ~~~~~~~~~~~~~~~~~~
"""
import unittest
from lib.feed import Feed


class TestFeed(unittest.TestCase):
    """
       Testes feed
    """

    def testFeedUrl(self):
        """
           Testa a url passada ao feed
        """
        feed = Feed('http://nl.com.br/blog/?feed=rss2')
        url = 'http://nl.com.br/blog/?feed=rss2'
        self.assertEqual( url, feed.url)

    def testFeedTitle(self):
        """
            Verifica se o feed contém um title válido
        """
        feed = Feed('http://nl.com.br/blog/?feed=rss2')
        self.assertTrue(feed.title)
