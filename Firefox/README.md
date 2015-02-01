Firefox tweaks
==============

Some tweaks for optimise Firefox...

About:config
------------

Some values to tweak on about:config.

* browser.sessionstore.interval 60000
* image.animation_mode: none
* network.prefetch-next: false

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
