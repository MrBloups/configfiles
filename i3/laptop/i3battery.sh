#!/bin/sh

if [ $# -ne 1 ]; then
    echo "Usage: $0 <i3 MODE>"
    exit 1
fi

MODE="$1"

STATUS="Discharging"
TIMER=5
MINI=5

PATH=/sys/class/power_supply/BAT1

show=false

while true
do
    bcapacity=`/usr/bin/cat $PATH/capacity`
    bstatus=`/usr/bin/cat $PATH/status`

    if [ "$bstatus" = "$STATUS" ]; then
        if [ "$bcapacity" -le $MINI ]; then
            if [ "$show" != true ]; then
                show=true
                /usr/bin/i3-msg mode $MODE
            fi
        fi
    fi

    /usr/bin/sleep $TIMER
done

exit 0
