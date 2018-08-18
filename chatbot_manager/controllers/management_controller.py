import connexion

from chatbot_manager.models.body import Body  # noqa: E501
from chatbot_manager.models.chatbot_full_info import ChatbotFullInfo  # noqa: E501
from chatbot_manager import util


def chatbot_id_delete(id, delete):  # noqa: E501
    """Deletes a chatbot

    Use the chatbot name to delete it # noqa: E501

    :param id: Name of the chatbot to delete
    :type id: str
    :param delete: JSON to confirm removing the chatbot
    :type delete: str

    :rtype: None
    """
    return 'do some magic!'


def chatbot_id_status_post(id, body):  # noqa: E501
    """Request a status change of the chatbot

    Use this to start or stop the chatbot # noqa: E501

    :param id: Name of the chatbot to change the status
    :type id: str
    :param body: JSON altering the \&quot;running\&quot; paramenter of the chatbot
    :type body: dict | bytes

    :rtype: ChatbotFullInfo
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
