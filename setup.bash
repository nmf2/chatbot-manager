#!/bin/bash

ensure_installed(){
    CMDS=$1
    for cmd in "$@"; do
        out=$(which $cmd)
        if [[ $out ]]; then
            echo "$cmd is installed."
        else
            echo "Please install $cmd"
            exit 1
        fi
    done
}

printf "Checking prerequisites\n\n"
ensure_installed docker docker-compose
printf "\nAll requisistes are installed.\n\n"

printf "Getting docker images\n\n"
docker pull nmf2/eva
docker pull nmf2/chatbot-api
docker pull docker.elastic.co/elasticsearch/elasticsearch-oss:6.2.4

printf "Creating ~/.chatbot-manager folder\n\n"
cd ~
mkdir .chatbot-manager
cd .chatbot-manager

printf ""