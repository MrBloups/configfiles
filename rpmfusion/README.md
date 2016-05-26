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

Note: Fedora pre-release repositories are available
---------------------------------------------------

Actually, these are the testing repo for Fedora 24:

    sudo dnf install --nogpgcheck http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-24.noarch.rpm
    sudo dnf install --nogpgcheck http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-24.noarch.rpm
