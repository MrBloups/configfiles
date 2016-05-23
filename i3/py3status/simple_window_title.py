# -*- coding: utf-8 -*-

"""
Display the current window title.

Requires:
    - i3-py (https://github.com/ziberna/i3-py)
    # pip install i3-py

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
    max_length = 100
    color = None

    def __init__(self):
        self.title = ''
        self.title_format = ''

    def simple_window_title(self, i3s_output_list, i3s_config):
        try:
            focused = i3.filter(focused=True)

            if len(focused) == 1:
                window = focused[0]

                if window['name'] != self.title:
                    self.title = window['name']
                    # title format
                    format = window['title_format']
                    self.title_format = format.replace('%title', '{title}')

                    if len(self.title) > self.max_length:
                        self.title =  "..." + self.title[-(self.max_length):]
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

    x = Py3status()

    while True:
        print(x.simple_window_title([], {}))
        sleep(1)
