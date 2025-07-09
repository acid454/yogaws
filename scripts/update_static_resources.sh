#!/bin/bash

ABSOLUTE_PATH=$(cd `dirname "${BASH_SOURCE[0]}"` && pwd)
RESOURCES_BASE="`readlink ${ABSOLUTE_PATH}/../ywsapp/static/ywsapp/res`"

[ -d ${HOME}/sounds-originals ] && {
    echo "Warning: extraction path ${HOME}/sounds-originals allready exists, please check and delete"
    exit  1
}

[ -d "$1" ] && {
    echo "Use sound files origin dir: $1"
    SOUND_ORIGIN="$1"
} || {
    echo "Unzip sounds from originals archive..."
    unzip ${RESOURCES_BASE}/../sounds-originals.zip -d ${HOME}
    SOUND_ORIGIN="${HOME}/sounds-originals"
}


rm -rf ${ABSOLUTE_PATH}/../ywsapp/static/ywsapp/res/sounds
mkdir -p "${ABSOLUTE_PATH}/../ywsapp/static/ywsapp/res/sounds"
${ABSOLUTE_PATH}/sound_installer.py "${SOUND_ORIGIN}"  "${ABSOLUTE_PATH}/../ywsapp/static/ywsapp/res/sounds"


rm -rf ${HOME}/sounds-originals
${ABSOLUTE_PATH}/gen_previews.py
