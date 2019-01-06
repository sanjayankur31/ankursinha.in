Finally checking out FlatPak
############################
:date: 2017-02-18 19:14:24
:author: ankur
:category: Tech
:tags: FlatPak, Fedora
:slug: finally-checking-out-flatpak
:summary: I've finally installed a few FlatPak_ applications to check the technology out.

I've been reading about FlatPak_ for a while now in various places (`Planet Fedora <http://planet.fedoraproject.org>`__) but I hadn't given it a try yet. I saw `Jiri's post on the planet <https://eischmann.wordpress.com/2017/02/15/nightly-and-wayland-builds-of-firefox-for-flatpak/>`__ earlier today and finally decided to install the Firefox Nightlies using FlatPak_. Of course, it works really well. I've gone ahead and installed the Telegram nightly from the `FlatPak website <http://flatpak.org/apps.html>`__ too.

The instructions are all there in the documentation `here <http://flatpak.org/apps.html>`__. It's really quite simple. On Fedora, first, you must have flatpak installed:

.. code:: bash

    sudo dnf install flatpak

Then, you go to the `FlatPak website <http://flatpak.org/apps.html>`__ and click on an app that you want to install. This opens up the Gnome Software centre that installs the application for you. The application then shows up in the list in the activities menu on Gnome. For Firefox, you can follow the instructions `here <https://firefox-flatpak.mojefedora.cz/>`__. For example, I now have the Firefox nightly installed:

.. image:: {static}/images/20170218-firefox-nightly-flatpak.png
    :align: center
    :target: {static}/images/20170218-firefox-nightly-flatpak.png
    :alt: Screenshot showing Firefox nightly FlatPak application
    :class: img-responsive

I now intend to make some time to learn more about FlatPak_ - I've read bits and pieces here and there about some of the great features it brings - sandboxing and so on - and it looks quite cool!

.. _FlatPak: http://flatpak.org
