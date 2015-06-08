Firefox tweaks
==============

Some tweaks for optimise Firefox...

Addons
------

* NoScripts
* HTTPS-Everywhere
* Ghostery
* Vimperator
* Quick Translator
* µBlock Origin (https://github.com/gorhill/uBlock)

About:config
------------

Some values to tweak on about:config.

* browser.sessionstore.interval: 60000
* image.animation_mode: none        # disable gif animation
* network.prefetch-next: false      # disable preload page
* loop.enabled: false               # disable ħello
* browser.newtabpage.{columns|rows} # for tweak about:newtab

Spell checking
--------------

Install hunspell packages on you system.
Exemple for fedora:

    [root]# yum install hunspell-fr

Stop GIF Image Animation
------------------------

Go to about:config and change the value of string **image.animation_mode** from **normal** to **none**.

Useful links
------------

* http://libre-ouvert.toile-libre.org/index.php?article207/optimiser-firefox-pour-les-petites-configurations
* http://martin.preisler.me/2014/08/h264-html5-video-in-firefox-on-fedora-20
