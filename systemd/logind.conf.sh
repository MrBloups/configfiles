#!/bin/sh

if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root" 1>&2
    exit 1
fi

LOGIND_CONF="/etc/systemd/logind.conf"

sed -i "/^\[Login\]/a KillUserProcesses=yes" $LOGIND_CONF
sed -i "/^\[Login\]/a ReserveVT=2" $LOGIND_CONF
sed -i "/^\[Login\]/a NAutoVTs=2" $LOGIND_CONF
