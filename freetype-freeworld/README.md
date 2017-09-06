rpmfusion repo must be enable.

install freetype-freeworld

    $ sudo dnf install freetype-freeworld

Configure freeworld for your session

    $ gsettings reset org.gnome.settings-daemon.plugins.xsettings rgba-order
    $ gsettings set org.gnome.settings-daemon.plugins.xsettings hinting slight
    $ gsettings set org.gnome.settings-daemon.plugins.xsettings antialiasing rgba
    
    $ cat >> $HOME/.Xresources << EOF
    Xft.lcdfilter: lcddefault
    EOF

