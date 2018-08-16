import connexion

from chatbot_manager.models.chatbot_basic_info import ChatbotBasicInfo  # noqa: E501
from chatbot_manager.models.chatbot_full_info import ChatbotFullInfo  # noqa: E501
from chatbot_manager import util


def chatbot_post(chatbot):  # noqa: E501
    """Creates a chatbot

    Creates a chatbot with a name (id) and description.  # noqa: E501

    :param chatbot: JSON object describing the chatbot to be created
    :type chatbot: dict | bytes

    :rtype: ChatbotFullInfo
    """
    if connexion.request.is_json:
        chatbot = ChatbotBasicInfo.from_dict(connexion.request.get_json())  # noqa: E501
        
    return 'do some magic!'
