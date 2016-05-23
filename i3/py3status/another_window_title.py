# -*- coding: utf-8 -*-

"""
Another module than display the current window title.
Use i3 title_format for display window title.

Limits:
    Don't support pango markup directives

Requires:
    - i3-py (https://github.com/ziberna/i3-py)
    # pip install [--user] i3-py

Configuration parameters:
    - cache_timeout : How often we refresh this module in seconds.
                      Default 0.5
    - color         : Color of printed text.
                      Default None
    - max_width     : Maximum width of block (in symbols).
                      If the title is longer than `max_width`,
                      it will be truncated.
                      Default: 120.

@author MrBloups
@license GPL
"""

import i3
from time import time


class Py3status:
    """
    """

    ## config parameters
    #
    cache_timeout = 0.5
    max_width = 120
    color = None

    def __init__(self):
        self.title = ''
        self.title_format = ''

    def another_window_title(self, i3s_output_list, i3s_config):
        try:
            focused = i3.filter(focused=True)

            if len(focused) == 1:
                window = focused[0]

                if window['name'] != self.title:
                    self.title = window['name']
                    # title format
                    format = window['title_format']
                    self.title_format = format.replace('%title', '{title}')

                    if len(self.title) > self.max_width:
                        self.title =  "..." + self.title[-(self.max_width):]
        except:
            self.title = ''
            self.title_format = ''
        finally:
            response = {
                'cached_until': time() + self.cache_timeout,
                'full_text': self.title_format.format(title=self.title),
                'color': self.color
            }
            return response

if __name__ == "__main__":
    """
    Test mode
    """

    from time import sleep

    i3s = Py3status()

    while True:
        print(i3s.another_window_title([], {}))
        sleep(2)
