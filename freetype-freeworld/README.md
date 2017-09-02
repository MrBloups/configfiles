rpmfusion repo must be enable.

install freetype-freeworld

    $ sudo dnf install freetype-freeworld

Configure freeworld for your session

    $ cat >> $HOME/.Xresources << EOF
    > Xft.lcdfilter: lcddefault
    > Xft.dpi: 96
    > Xft.hinting: 1
    > Xft.hintstyle: hintslight
    > Xft.lcdfilter: lcddefault
    > Xft.antialias: 1
    > Xft.rgba: rgb
    > EOF

