# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from chatbot_manager.models.body import Body  # noqa: E501
from chatbot_manager.models.chatbot_full_info import ChatbotFullInfo  # noqa: E501
from chatbot_manager.test import BaseTestCase


class TestManagementController(BaseTestCase):
    """ManagementController integration test stubs"""

    def test_chatbot_id_delete(self):
        """Test case for chatbot_id_delete

        Deletes a chatbot
        """
        query_string = [('delete', 'delete_example')]
        response = self.client.open(
            '/nmf21/ChatbotManager/1.0.0/chatbot/{id}'.format(id='id_example'),
            method='DELETE',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_chatbot_id_status_post(self):
        """Test case for chatbot_id_status_post

        Request a status change of the chatbot
        """
        body = Body()
        response = self.client.open(
            '/nmf21/ChatbotManager/1.0.0/chatbot/{id}/status'.format(id='id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
