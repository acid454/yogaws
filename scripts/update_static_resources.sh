#!/bin/bash

ABSOLUTE_PATH=$(cd `dirname "${BASH_SOURCE[0]}"` && pwd)
RESOURCES_BASE="`readlink ${ABSOLUTE_PATH}/../ywsapp/static/ywsapp/res`"
rm -rf ${ABSOLUTE_PATH}/../ywsapp/static/ywsapp/res/sounds
rm -rf ${HOME}/sounds-originals

unzip ${RESOURCES_BASE}/../sounds-originals.zip -d ${HOME}
mkdir -p "${ABSOLUTE_PATH}/../ywsapp/static/ywsapp/res/sounds"
${ABSOLUTE_PATH}/sound_installer.py "${HOME}/sounds-originals" "${ABSOLUTE_PATH}/../ywsapp/static/ywsapp/res/sounds"

rm -rf ${HOME}/sounds-originals
