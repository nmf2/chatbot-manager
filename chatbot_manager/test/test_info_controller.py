# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from chatbot_manager.models.chatbot_full_info import ChatbotFullInfo  # noqa: E501
from chatbot_manager.test import BaseTestCase


class TestInfoController(BaseTestCase):
    """InfoController integration test stubs"""

    def test_chatbot_id_get(self):
        """Test case for chatbot_id_get

        Get info about some chatbot
        """
        response = self.client.open(
            '/nmf21/ChatbotManager/1.0.0/chatbot/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_chatbot_id_status_get(self):
        """Test case for chatbot_id_status_get

        Check if the chatbot is running
        """
        response = self.client.open(
            '/nmf21/ChatbotManager/1.0.0/chatbot/{id}/status'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
