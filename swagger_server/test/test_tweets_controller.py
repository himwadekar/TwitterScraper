# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.tweets import Tweets  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTweetsController(BaseTestCase):
    """TweetsController integration test stubs"""

    def test_tweets_using_hashtag(self):
        """Test case for tweets_using_hashtag

        Scrape tweets using hashtag
        """
        query_string = [('status', 'available')]
        response = self.client.open(
            '/tweets_by_hashtag',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_tweets(self):
        """Test case for user_tweets

        Scrape user tweets
        """
        query_string = [('status', 'available')]
        response = self.client.open(
            '/user_tweets',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
