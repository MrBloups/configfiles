# -*- coding:utf-8 -*-

from dialog import Dialog

class DialogInstall(Dialog):

    def __init__(self):
        super(DialogInstall, self).__init__()

    def checklist_modules(self):
        c = []
        c.append(('Gtk3', 'GTK3 theme', True))
        c.append(('bashrc', 'Bashrc config', True))
        c.append(('Vim', 'Vim config and theme', True))
        c.append(('URxvt', 'URxvt config and theme', True))
        c.append(('i3', 'i3wm config and theme', True))
        c.append(('git', 'Git config', True))
        c.append(('firefox', 'Firefox config', True))
        c.append(('lightdm', 'LightDM config and theme', True))
        c.append(('sys', 'Systeme config for Ideapad S300', True))

        self.checklist("Choose modules to install",
                       choices = c,
                       width = 80, height = 25, list_height = 20)

if __name__ == '__main__':

    d = DialogInstall()
    d.set_background_title("Configfile")
    d.checklist_modules()
