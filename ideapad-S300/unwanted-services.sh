#!/bin/sh

## oneshot

systemctl disable abrt-ccpp.service
systemctl disable abrt-oops.service
systemctl disable abrt-xorg.service
systemctl disable abrt-vmcore.service
systemctl disable abrtd.service
systemctl disable accounts-daemon.service
systemctl disable atd.service
systemctl disable auditd.service
systemctl disable crond.service
systemctl disable cups.service
systemctl disable iscsi.service
systemctl disable sendmail.service
systemctl disable sm-client.service
systemctl disable bluetooth.service
systemctl disable libvirtd.service
systemctl disable rngd.service
systemctl disable rsyslog.service
systemctl disable lvm2-monitor.service
systemctl disable mdmonitor.service
systemctl disable avahi-daemon.service
systemctl disable multipathd.service
systemctl disable dmraid-activation.service
systemctl disable sshd.service

systemctl disable spice-vdagentd.service
systemctl disable iscsid.socket
systemctl disable iscsiuio.socket
systemctl disable vmtoolsd.service
#systemctl disable timedatex.service
systemctl disable rpcbind.socket


