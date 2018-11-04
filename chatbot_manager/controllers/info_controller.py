from chatbot_manager.models.chatbot_full_info import ChatbotFullInfo  # noqa: E501
from pathlib import Path
import json
from chatbot_manager.util import get_base_path


def chatbot_id_get(id):  # noqa: E501
    """Get info about some chatbot

    By using the correct parameters get information about a particular chatbot # noqa: E501

    :param id: Name of the chatbot to query
    :type id: str

    :rtype: ChatbotFullInfo
    """
    try:
        base = get_base_path(id)
        #print(base)
        if not base.exists():
            res = "chatbot not found"
            code = 404
        else:
            path = base / Path('info.json')
            with path.open('r') as info_file:
                chatbot = json.load(info_file)
            res = ChatbotFullInfo(**chatbot)
            code = 200
    except:
        res = "unknown error, contact developer"
        code = 500
    return res, code


def chatbot_id_status_get(id):  # noqa: E501
    """Check if the chatbot is running

    Checks if the chatbot is currently running # noqa: E501

    :param id: Name of the chatbot to change the status
    :type id: str

    :rtype: ERRORUNKNOWN
    """

    res, code = chatbot_id_get(id)
    if type(res) == ChatbotFullInfo:
        info = res.to_dict()
        res = {'running': info['running']}

    return res, code
