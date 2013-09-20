#!/bin/bash
#

APPNAME="boilerplate-app"
USERNAME="username"
SERVER="server.domain.com"
DST_PROD="/srv/$APPNAME/webapp"
DST_DEV="/srv/$APPNAME/dev"

if [ "x$1" == "x" ]; then
    DST_DIR=$DST_DEV;
    echo -en "Deploying to development..\t"
elif [ "$1" == "-d" ]; then
    DST_DIR=$DST_PROD;
    echo -en "Deploying to production..\t"
fi;

scp -qr * $USERNAME@$SERVER:$DST_DIR && echo "OK" || echo "FAIL"

