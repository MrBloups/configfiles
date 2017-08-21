Tweaks
======

Gnome-setting-daemon
--------------------

You can use gnome-settings-daemon for better integration.
In your **~/.i3/config**, add:

    exec --no-startup-id /usr/libexec/gnome-settings-daemon

If your cursor is invisible, run in a terminal:

    dconf write /org/gnome/settings-daemon/plugins/cursor/active false

Gnome-terminal
--------------

For disable blink cursor, run in a terminal:

    gsettings set org.gnome.desktop.interface cursor-blink false

Inserting a Unicode character in VIM
------------------------------------

In INSERT MODE type:

    Ctrl + v, u, unicode code

See
---

https://faq.i3wm.org/question/4126/sessions-environment-variables.1.html
