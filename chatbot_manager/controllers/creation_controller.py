from pathlib import Path
from datetime import datetime
import json
from chatbot_manager.models.chatbot_full_info import ChatbotFullInfo  # noqa: E501
from chatbot_manager.util import get_base_path, create_docker_compose


def chatbot_post(chatbot):  # noqa: E501
    """Creates a chatbot

    Creates a chatbot with a name (id) and description.  # noqa: E501

    :param chatbot: JSON object describing the chatbot to be created
    :type chatbot: dict | bytes

    :rtype: ChatbotFullInfo
    """
    try:
        base = get_base_path(chatbot['id'])
        if base.exists():
            res = "a chatbot with the same id already exists"
            code = 409
        else:
            base.mkdir(parents=True)

            for folder in ['data/iob', 'models/', '../elasticsearch']:
                path = base / Path(folder)
                path.mkdir(parents=True)

            chatbot.update({
                'running': False,
                'created': str(datetime.now()),
                'address': ''
            })

            # Write Chatbot Manager level info
            path = base.parent / Path('info.json')
            with path.open('w') as info_file:
                json.dump(chatbot, info_file)

            # Write Chatbot level info
            path = base / Path('info.json')
            with path.open('w') as info_file:
                json.dump({
                    'id': chatbot['id'],
                    'description': chatbot['description'],
                    'created': chatbot['created'],
                }, info_file)

            create_docker_compose(chatbot['id'])

            res = ChatbotFullInfo(**chatbot)
            code = 201
    except(KeyError):
        res = "Bad body input"
        code = 400
    except:
        res = "unkown error, contact developer"
        code = 500

    return res, code
