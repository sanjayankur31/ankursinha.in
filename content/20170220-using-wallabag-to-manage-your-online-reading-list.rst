Using Wallabag to manage your online reading list
#################################################
:date: 2017-02-28 20:52:40
:author: ankur
:category: Tech
:tags: Fedora, Wallabag, Planet, Reading
:slug: using-wallabag-to-manage-your-online-reading-list
:summary: I've recently begun using Wallabag_ to manage my reading list. It is released under the `MIT license`_, so it's `Free software`_ too!


Edit (28 February 2017): Earlier today, it was `announced that Mozilla had acquired Pocket <https://blog.mozilla.org/blog/2017/02/27/mozilla-acquires-pocket/>`__ with `plans to gradually release the Pocket source code under Open Source licenses <https://bugzil.la/1343006>`__.  I guess Wallabag_ will remain as a self hosted solution, but given an improved integration of Pocket with Firefox, I may move back to it in the near future.

------

I always have quite a bit on my pending list to read - academic papers, blogs, planets, and the sort. Usually, when I go through the planets, such as the `Fedora <http://fedoraplanet.org/>`__, `GNOME <http://planet.gnome.org/>`__ or the two neuroscience planets I use - `neuroscience <https://sanjayankur31.github.io/planet-neuroscience/>`__, `neuroscientists <https://sanjayankur31.github.io/planet-neuroscientists/>`__, I don't have the time to read all the articles right then. I used to either bookmark links, or note them down somewhere to read later. One day, though, I ran into Pocket_, which lets you save the article to read later and makes it available to you on multiple devices. It's extremely convenient.

Of course, the one issue with Pocket_ is that it isn't `Free software`_. So, like I do, I went looking for an alternative. After a few hours, I ran into Wallabag_ on `Github <https://github.com/wallabag/wallabag>`__. It's written in PHP, and is licensed under the `MIT license`_. It's quite easy to deploy, and there's a `Gitter channel <https://gitter.im/wallabag/wallabag>`__ where you can get some help too. 

You either enter the URL in the Wallabag page manually, or you can use the `Firefox <https://addons.mozilla.org/firefox/addon/wallabagger/>`__/`Chrome <https://chrome.google.com/webstore/detail/wallabagger/gbmgphmejlcoihgedabhgjdkcahacjlj>`__/`Opera <https://addons.opera.com/en/extensions/details/wallabagger/?display=en>`__ addon - it let's you right click a page or a link and "Wallabag.it!". There's also a bookmarklet, which you can use with `Pentadactyl <https://github.com/5digits/dactyl>`__, for example:

.. code:: bash

    # Add to ~/.pentadactylrc
    command! wallabagit -description "Add to wallabag" open javascript:(function(){var%20url=location.href||url;var%20wllbg=window.open('https://app.wallabag.it/bookmarklet?url='%20+%20encodeURI(url),'_blank');})();

Wallabag fetches the text of the page and stores it for you so that you can read it later. You can even organise your saved pages with tags and the sort.

.. image:: {static}/images/20170220-wallabag.png
    :align: center
    :target: {static}/images/20170220-wallabag.png
    :alt: Screenshot showing the Wallabag main page
    :class: img-responsive

Here's a page that I'm trying to read later, for example:

.. image:: {static}/images/20170220-wallabag-2.png
    :align: center
    :target: {static}/images/20170220-wallabag-2.png
    :alt: Screenshot showing an article in Wallabag
    :class: img-responsive

I played with a deployment, but decided not to deploy and maintain an instance myself. Instead, I signed up for the instance Wallabag have here - `Wallabag.it <https://www.wallabag.it/en>`__. It's quite cheap - they have an offer going too at the moment - `only 9€ for an entire year <https://wallabag.org/en/news/wallabagit>`__!


Wallabag uses a the `FiveFilters Full Text RSS tool <http://fivefilters.org/content-only/>`__ to extract the text and other data from web pages. Some websites require special instructions to tell the tool what information needs to be extracted - this tends to happen with a few academic websites. There's a `repository of such config files here <https://github.com/fivefilters/ftr-site-config>`__. So, if you do run into a website that isn't rendering properly, you can `troubleshoot the issue and submit a config file too <http://doc.wallabag.org/en/master/user/errors_during_fetching.html>`__.

Whether you decide to deploy an instance yourself, or use `Wallabag.it <https://www.wallabag.it/en>`__, I think it's a really useful tool to have. Of course, don't forget to install the `app on your phone <https://play.google.com/store/apps/details?id=fr.gaulupeau.apps.InThePoche&hl=en>`__ too!

Happy reading!

.. _Pocket: getpocket.com/
.. _MIT license: https://tldrlegal.com/license/mit-license
.. _Free software: https://www.gnu.org/philosophy/free-sw.en.html
.. _Wallabag: https://wallabag.org/en
