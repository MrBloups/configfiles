# -*- coding: utf-8 -*-

"""
awesome module than display the current window title.
Use i3 title_format for display window title.

Limits:
    Don't support pango markup directives

Requires:
    - i3-py (https://github.com/ziberna/i3-py)
    # pip install [--user] i3-py

Configuration parameters:
    - cache_timeout : How often we refresh this module in seconds.
                      Default 0.5
    - prefix        : an optional string for print something before title
    - color         : Color of printed text.
                      Default None
    - max_width     : Maximum width of block (in symbols).
                      If the title is longer than `max_width`,
                      it will be truncated.
                      Default: 100.

@author MrBloups
@license GPL
"""

from time import time, sleep
from subprocess import PIPE, Popen


class Py3status:
    """
    """

    ## config parameters
    #
    cache_timeout = 0.5
    color = None

    def __init__(self):
        self.full_text = u''
        self.root_check = ''

    def __get_visible_title(self):
        title = ""
        root = Popen(["xprop","-root"], stdout=PIPE)

        if root.stdout != self.root_check:
            self.root_check = root.stdout
            # current window
            for i in root.stdout:
                i = i.decode('utf-8').strip()
                if i.startswith("_NET_ACTIVE_WINDOW(WINDOW)"):
                    id_ = i.split()[4]
                    id_w = Popen(['xprop', '-id', id_], stdout=PIPE)
                    break
            # current title of current window
            for j in id_w.stdout:
                j = j.decode('utf-8').strip()
                if j.startswith('_NET_WM_VISIBLE_NAME(UTF8_STRING)'):
                    title = j.replace('_NET_WM_VISIBLE_NAME(UTF8_STRING) = ', '')
                    break

        return title[1:-1]

    def awesome_window_title(self, i3s_output_list, i3s_config):
        try:
            # title
            self.full_text = self.__get_visible_title()
            #self.color = i3s_config["color_good"]
        except Exception as e:
            self.full_text = u"#ERR {}".format(e)
            self.color = i3s_config["color_bad"]
        finally:
            response = {
                'cached_until': time() + self.cache_timeout,
                'full_text': self.full_text,
                'color': self.color
            }
            return response

if __name__ == "__main__":
    """
    Test mode
    """
    i3s = Py3status()

    while True:
        print(i3s.awesome_window_title([], {}))
        sleep(2)
