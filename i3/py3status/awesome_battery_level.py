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

from time import time


class Py3status:
    """
    """
    cache_timeout = 5
    color = None
    battery_name = "BAT1"

    def __init__(self):
        """
        """
        self.full_text = ""
        self.path_uevent = "/sys/class/power_supply/{}/uevent".format(self.battery_name)
        self.uevent = {}
        # battery level icon
        self.icons = {}
        self.icons[5]   = ""
        self.icons[35]  = ""
        self.icons[70]  = ""
        self.icons[85]  = ""
        self.icons[100] = ""
        # color alert
        self.danger = 5
        self.warning = 20

    def _get_time_remaining(self):
        charge_full = int(self.uevent["POWER_SUPPLY_ENERGY_FULL"])
        charge_now = int(self.uevent["POWER_SUPPLY_ENERGY_NOW"])
        current_now = int(self.uevent["POWER_SUPPLY_POWER_NOW"])

        return (charge_full - charge_now) / current_now

    def _update_uevent(self):
        """
        """
        self.uevent = {}
        with open(self.path_uevent, "r") as uevent:
            for line in uevent:
                item = line.split("=")
                if len(item) == 2:
                    self.uevent[item[0].strip()] = item[1].strip()

    def _update_awesome(self, config):
        """
        """
        capacity = int(self.uevent["POWER_SUPPLY_CAPACITY"])
        status = self.uevent["POWER_SUPPLY_STATUS"]

        color = config["color_good"] if status == "Full" else None
        charging = True if status == "Charging" else False
        charging_glyphe = " ⚡" if charging else ""

        # define icon
        icon = None
        for level in sorted(self.icons):
            if capacity <= level:
                icon = self.icons[level]
                break

        if not charging:
            if capacity <= self.danger:
                icon = icon + "  "
                color = config["color_bad"]
            elif capacity <= self.warning:
                color = config["color_degraded"]

        self.full_text = "{}{}  {}%".format(icon, charging_glyphe, capacity)
        self.color = color


    def awesome_battery_level(self, i3s_output_list, i3s_config):
        """
        """
        try:
            self._update_uevent()
            self._update_awesome(i3s_config)
        except :
            self.full_text = ""
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

    from time import sleep

    i3s = Py3status()
    conf = { "color_bad": "#FF0000",
             "color_degraded": "#0000FF",
             "color_good": "#00FF00"}

    while True:
        print(i3s.awesome_battery_level([], conf))
        sleep(2)
