#!/usr/bin/env python3

import connexion
import socket

from chatbot_manager import encoder


def get_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    port = sock.getsockname()[1]
    sock.close()
    return port


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Simple Inventory API'})
    app.run(port=55555, debug=True)


if __name__ == '__main__':
    main()
