RPMFUSION
=========

Install repo and codecs from rpmfusion

    # install rpmfusion repo
    dnf install http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
    dnf install http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

    # install codecs
    dnf install gstreamer1-{libav,vaapi} gstreamer1-plugins-{good,good-extras,ugly}
    # optional codecs
    dnf install gstreamer1-plugins-bad-{free,freeworld}
