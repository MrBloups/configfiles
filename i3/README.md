TIPS
====

Gnome-setting-daemon
--------------------

You can use gnome-settings-daemon for better integration.  
In your ~/.i3/config, add:

    exec --no-startup-id /usr/libexec/gnome-settings-daemon

If your cursor is invisible, run in a terminal:  

    dconf write /org/gnome/settings-daemon/plugins/cursor/active false
