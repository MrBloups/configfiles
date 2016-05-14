configfiles
===========

Repository for configuration files and scripts on Fedora 22

Laptop power management
-----------------------

Some useful links
* https://docs.fedoraproject.org/en-US/Fedora/15/html/Power_Management_Guide/Example_Laptop.html
* http://doc.fedora-fr.org/wiki/Optimisation_de_l%27autonomie_de_son_portable_ou_de_son_netbook
* http://www.thinkwiki.org/wiki/How_to_reduce_power_consumption
* http://doc.fedora-fr.org/wiki/Les_SSD_sous_fedora

Disable gdm user list
---------------------

    sudo -u gdm dbus-launch gsettings set org.gnome.login-screen disable-user-list true

Complete localisation installation
----------------------------------

    # dnf install dnf-langpacks
    # dnf langinstall fr

System upgrading
----------------

    # dnf upgrade
    # dnf install dnf-plugin-system-upgrade
    # dnf system-upgrade download --releaserver=24 --allowerasing

Use '--allowerasing' if you have additional repo (rpmfusion for example).

    # dnf system-upgrade reboot

And let you PC restart. It boot on your last kernel...

See
* https://fedoraproject.org/wiki/DNF_system_upgrade
