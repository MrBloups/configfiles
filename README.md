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

Disable Wayland from gdm
------------------------

    sed -i '/^#WaylandEnable/a WaylandEnable=false' /etc/gdm/custom.conf

Use xcalib
----------

Xcalib is a tool for calibrate your screen manually or from an icc profile. Install it.

    sudo dnf install xcalib

Get the icc profile for your screen back.

    wget http://www.notebookcheck.net/uploads/tx_nbc2/Lenovo_S300_glare_1366x768__LG_Display_LP133WH2_TLE1_.icc

And use

    xcalib -clear ; xcalib ICCPROFILE

Manage wifi connexion with nmcli
--------------------------------

Make sure you are NetworkManager for Wifi

    dnf install NetworkManager-wifi network-manager-applet gnome-keyring

In dot bash_profile add

    if [ -n "$DESKTOP_SESSION" ]; then
        eval `gnome-keyring-daemon --start --components=secret`
        export SSH_AUTH_SOCK
    fi

Restart your session. Run nm-applet.

Next, create and configure your connexion

    nmcli con dev wifi list con-name YOUR_CON_NAME ifname YOUR_INTERFACE type wifi ssid YOUR_SSID
    nmcli con modify MonWifi 802-11-wireless.hidden yes
    nmcli con modify MonWifi wifi-sec.key-mgmt wpa-psk
    nmcli con modify MonWifi wifi-sec.psk YOUR_PASSWORD
    
    nmcli con up YOUR_CON_NAME

TIPS nm-connection-editor:
In 'General' tab, check connection auto and all user
In 'Security' tab, check password for all user (under bottom arrow in passwor field)


Complete localisation installation
----------------------------------

    dnf install dnf-langpacks
    dnf langinstall fr

Enable powertop service
-----------------------

    dnf install powertop
    powertop --calibrate
    systemctl enable powertop
    systemctl start powertop

