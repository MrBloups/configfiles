FEDORA 21
=========

Additionnal repo
----------------
    [root]# yum install http://linuxdownload.adobe.com/adobe-release/adobe-release-x86_64-1.0-1.noarch.rpm

RPM
---
    [root]# yum install gnome-tweak-tool faience-icon-theme terminus-fonts
    [root]# yum install vim-enhanced man-pages-fr git gcc
    [root]# yum install i3 i3status i3lock unclutter epiphany
    [root]# yum install powertop rfkill preload xbacklight
    [root]# yum install newsbeuter
    [root]# yum install flash-plugin
    [root]# yum install mozilla-https-everywhere mozilla-noscript

Systemd
--------
journald in RAM

    [root]# sed -i "/#Storage=auto/a Storage=volatile" /etc/systemd/journald.conf

Only 2 tty

    [root]# sed -i "/#NAutoVTs=6/a NAutoVTs=2" /etc/systemd/logind.conf


Grub2
-----
Fullscreen grub menu

    [root]# sed -i '/GRUB_TERMINAL_OUTPUT/ s/^/#/' /etc/default/grub
    [root]# sed -i '/GRUB_CMDLINE_LINUX/ s/^/#/' /etc/default/grub
    [root]# sed -i '/GRUB_CMDLINE_LINUX/a GRUB_CMDLINE_LINUX="rhgb quiet i915.lvds_downclock=1 i915.enable_fbc=1 i915.enable_rc6=7 drm.vblankoffdelay=1"' /etc/default/grub
    [root]# grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg

Yum
---
Backup two kernels instead of three

    [root]# sed -i '/^installonly_limit/ s/2/3/' /etc/yum.conf

Selinux
-------
    [root]# sed -i '/^SELINUX=/ s/enforcing/disabled/' /etc/selinux/config

Fstab
-----
    [root]# sed -i '/ext4/ s/defaults/defaults,lazytime/' /etc/fstab
    [root]# sed -i '/ext4/ s/1 1$/0 1/' /etc/fstab
    [root]# sed -i '/ext4/ s/1 2$/0 2/' /etc/fstab

Gdm
---
Disable user list

    [root]# sudo -u gdm dbus-launch gsettings set org.gnome.login-screen disable-user-list true
