Firefox tweaks
==============

Some tweaks for optimise Firefox...

Addons
------

* Ghostery
* µBlock Origin (https://github.com/gorhill/uBlock)

About:config
------------

Some values to tweak on about:config.

* browser.sessionstore.interval: 60000
* image.animation_mode: none        # disable gif animation
* network.prefetch-next: false      # disable preload page
* loop.enabled: false               # disable Hello
* browser.pocket.enabled: false     # disable Pocket
* browser.newtabpage.{columns|rows} # for tweak about:newtab

Spell checking
--------------

Install hunspell packages on you system.
Exemple for fedora:

    [root]# yum install hunspell-fr


Don't close window with last tab
--------------------------------

In about:config change the value of **browser.tabs.closeWindowWithLastTab** from true to **false**.

Always enabled tracking protection (Firefox 42 and later)
---------------------------------------------------------

In about:config change the value of **privacy.trackingprotection.enabled** from false to **true**.

Stop GIF Image Animation
------------------------

Go to about:config and change the value of string **image.animation_mode** from **normal** to **none**.

Disable media auto play
-----------------------

Go to about:config and change the value of string **media.autoplay.enabled** from **normal** to **false**.


Graphics acceleration with Skia
-------------------------------

* gfx.content.azure.backends: skia # default cairo

Force enable e10s
-----------------

Go to about:config and add a new boolean pref : browser.tabs.remote.force-enable = true

Useful links
------------

* http://libre-ouvert.toile-libre.org/index.php?article207/optimiser-firefox-pour-les-petites-configurations
* http://martin.preisler.me/2014/08/h264-html5-video-in-firefox-on-fedora-20
