# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.chatbot_basic_info import ChatbotBasicInfo  # noqa: E501
from swagger_server.models.chatbot_full_info import ChatbotFullInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCreationController(BaseTestCase):
    """CreationController integration test stubs"""

    def test_chatbot_post(self):
        """Test case for chatbot_post

        Creates a chatbot
        """
        chatbot = ChatbotBasicInfo()
        response = self.client.open(
            '/nmf21/ChatbotManager/1.0.0/chatbot',
            method='POST',
            data=json.dumps(chatbot),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
