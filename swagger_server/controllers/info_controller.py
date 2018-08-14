import connexion
import six

from swagger_server.models.chatbot_full_info import ChatbotFullInfo  # noqa: E501
from swagger_server.models.errorunknown import ERRORUNKNOWN  # noqa: E501
from swagger_server import util


def chatbot_id_get(id):  # noqa: E501
    """Get info about some chatbot

    By using the correct parameters get information about a particular chatbot # noqa: E501

    :param id: Name of the chatbot to query
    :type id: str

    :rtype: ChatbotFullInfo
    """
    return 'do some magic!'


def chatbot_id_status_get(id):  # noqa: E501
    """Check if the chatbot is running

    Checks if the chatbot is currently running # noqa: E501

    :param id: Name of the chatbot to change the status
    :type id: str

    :rtype: ERRORUNKNOWN
    """
    return 'do some magic!'
