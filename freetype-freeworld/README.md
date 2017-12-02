rpmfusion repo must be enable.

install freetype-freeworld

    $ sudo dnf install freetype-freeworld

Configure ldc filter for the system

    # ln -s /usr/share/fontconfig/conf.avail/11-lcdfilter-default.conf /etc/fonts/conf.d/

Configure freeworld for your session

    $ gsettings reset org.gnome.settings-daemon.plugins.xsettings rgba-order
    $ gsettings set org.gnome.settings-daemon.plugins.xsettings hinting slight
    $ gsettings set org.gnome.settings-daemon.plugins.xsettings antialiasing rgba

    $ echo "Xft.lcdfilter: lcddefault" > ~/.Xresources
