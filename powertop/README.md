Enable power saving with powertop.

Enable powertop service
-----------------------

    dnf install powertop
    powertop --calibrate
    systemctl enable powertop
    systemctl start powertop

