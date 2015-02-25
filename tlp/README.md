Install and enable tlp
----------------------

### Install

    sudo yum install tlp tlp-rdw smartmontools

### Enable

    systemctl mask systemd-rfkill
    systemctl enable tlp
    systemctl start tlp
