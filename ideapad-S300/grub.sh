#!/bin/sh

grub_file='/etc/default/grub'

sed 's/GRUB_TERMINAL_OUTPUT/ s/^/#/' $grub_file
sed 's/GRUB_CMDLINE_LINUX/ s/quiet/quiet i915.modeset=1 i915.semaphores=1 i915.enable_rc6=1 i915.enable_fbc=1/' $grub_file

exit 0
