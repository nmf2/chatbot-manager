from chatbot_manager import util


import docker
import subprocess
import shutil



def chatbot_id_delete(id, delete):  # noqa: E501
    """Deletes a chatbot

    Use the chatbot name to delete it # noqa: E501

    :param id: Name of the chatbot to delete
    :type id: str
    :param delete: JSON to confirm removing the chatbot
    :type delete: str

    :rtype: None
    """
    try:
        base = util.get_base_path(id)
        if not base.parent.exists():
            res = "Chatbot Not Found"
            code = 404
        elif delete:
            path = base.parent
            shutil.rmtree(str(path))

            res = "Chatbot Deleted"
            code = 200
    except:
        res = "Unknow error, contact developer"
        code = 500

    return res, code


def chatbot_id_status_post(id, body):  # noqa: E501
    """Request a status change of the chatbot

    Use this to start or stop the chatbot # noqa: E501

    :param id: Name of the chatbot to change the status
    :type id: str
    :param body: JSON altering the \&quot;running\&quot; paramenter of the chatbot
    :type body: dict | bytes

    :rtype: ChatbotFullInfo
    """
    try:
        base = util.get_base_path(id)
        if not base.exists():
            res = "Chatbot Not Found"
            code = 404
        elif body["running"] is True:  
            path = str(base.parent) + '/docker-compose.yml'
            #print("docker-compose up -d -f {}".format(path).split())
            subprocess.call("docker-compose -f {} up -d".format(path).split())

            bot, es = _get_containers(id)

            bot_addr = _get_container_addr(bot, '8080/tcp')
            es_addr = _get_container_addr(es, '9200/tcp')
            address = bot_addr + ',' + es_addr

            info_file = util.get_info_file(id, glob=True)
            util.update_info_file(info_file, address=address, running=True)

            res = "OK, Chatbot Running"
            code = 200
        else:
            # Stop a chatbot
            _stop_chatbot(id)

            res = "OK, Chatbot Stopped"
            code = 200

    except KeyError:
        raise
        res = "Bad request body"
        code = 400
    except docker.errors.NotFound:
        raise
        res = "Chatbot Not Found"
        code = 404
    except:
        raise
        res = "Unknown error, contact developer"
        code = 500
    return res, code


def _get_container_addr(container, port):

    ip = container.attrs['NetworkSettings']['Ports'][port][0]['HostIp']
    hostport = container.attrs['NetworkSettings']['Ports'][port][0]['HostPort']

    return ip + ':' + hostport


def _get_containers(chatbot):
    client = docker.from_env()
    bot = client.containers.get(chatbot)
    es = client.containers.get("elasticsearch_" + chatbot)

    return bot, es


def _stop_chatbot(chatbot, force=False):
    bot, es = _get_containers(chatbot)

    if force:
        bot.kill()
        es.kill()
    else:
        bot.stop()
        es.stop()

    info_file = util.get_info_file(chatbot, glob=True)
    util.update_info_file(info_file, address='', running=False)

    return bot, es