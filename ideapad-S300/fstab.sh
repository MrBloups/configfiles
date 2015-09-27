#!/usr/bin/sh

FSTAB='/etc/fstab'

cp $FSTAB $FSTAB.1

if [ $? -eq 0 ]; then
    sed -i '/ext4/ s/defaults/defaults,lazytime/' $FSTAB
    sed -i '/ext4/ s/1 1$/0 1/' $FSTAB
    sed -i '/ext4/ s/1 2$/0 2/' $FSTAB
fi
