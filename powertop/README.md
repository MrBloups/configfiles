Enable power saving with powertop.

Enable powertop service
-----------------------

    # dnf install powertop
    # powertop --calibrate
    -- standard
    # systemctl enable powertop
    # systemctl start powertop

If all tunes are not ok. Disable powertop service and enable rc-local service.
In a /etc/rc.d/rc.local (chmod 755) file add 'powertop --auto-tune'.

    # systemctl disable powertop
    # systemctl stop powertop

    # systemctl enable rc-local
    # vim /etc/rc.d/rc.local
      powertop --auto-tune 2>/dev/null


