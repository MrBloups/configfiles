FEDORA 23
=========

RPM
---
    [root]# yum install gnome-tweak-tool faience-icon-theme terminus-fonts
    [root]# yum install vim-enhanced man-pages-fr git
    [root]# yum install i3 i3status i3lock
    [root]# yum install powertop preload
    [root]# yum install newsbeuter

Systemd
--------

Only 2 tty

    [root]# sed -i "/#NAutoVTs=6/a NAutoVTs=2" /etc/systemd/logind.conf


Grub2
-----
Fullscreen grub menu

    [root]# sed -i '/GRUB_TERMINAL_OUTPUT/ s/^/#/' /etc/default/grub
    [root]# sed -i '/GRUB_CMDLINE_LINUX/ s/^/#/' /etc/default/grub
    [root]# sed -i '/GRUB_CMDLINE_LINUX/a GRUB_CMDLINE_LINUX="rhgb quiet i915.lvds_downclock=1 i915.enable_fbc=1 i915.enable_rc6=7 drm.vblankoffdelay=1"' /etc/default/grub
    [root]# sed -i '/GRUB_SAVED/a GRUB_SAVEDEFAULT=true' /etc/default/grub
    [root]# grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg

DNF
---
Backup two kernels instead of three

    [root]# sed -i '/^installonly_limit/ s/2/3/' /etc/dnf/dnf.conf

Selinux
-------
    [root]# sed -i '/^SELINUX=/ s/enforcing/disabled/' /etc/selinux/config

Gdm
---
Disable user list

    [root]# sudo -u gdm dbus-launch gsettings set org.gnome.login-screen disable-user-list true
