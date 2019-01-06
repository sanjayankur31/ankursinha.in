Using your gnotes on your android phone
#######################################
:date: 2011-09-30 01:18
:author: ankur
:category: Tech
:tags: Android
:slug: using-your-gnotes-on-your-android-phone
:summary: Using Gnotes on your Android phone.


.. image:: {static}/images/gnote.png
    :alt: Gnote icon

.. image:: {static}/images/swiftp.jpg
    :alt: swiftp icon

.. image:: {static}/images/tomdroid.jpg
    :alt: tomdroid icon

I recently came across this tutorial which dealt with `using Gnote to
unclutter one's daily note`_\ s. It really is a great post. I adopted
the organizational scheme instantly. Now, being a curious person, I went
hunting for ways to use these notes with my android phone. I've found a
way which I'll detail below.

First, install `Gnote`_. On a fedora system, this is as simple as

.. code-block:: bash

    su -c 'yum install gnote'

Then, head to the android market, and install `Tomdroid`_ on your
Android phone.

Here's what needs to be done:

-  Make your notes in Gnote. They are stored in **~/.local/share/gnote**
-  Copy the notes to a **tomdroid** folder in your **sdcard root** on
   your **Android phone**. Create the folder if it doesn't exist by
   default.
-  In Tomdroid, hit menu to go to the preferences. Here, select "SD
   Card" in the sync preferences.
-  Get to the Tomdroid main screen, and tap the sync icon.
-  That's all!

That was part I. Here is part II: How to transfer your notes to your
phone. Some of you might like to hook your phone up using the USB, but I
find that just a tad bit tedious. I prefer using my wifi connection to
transfer this data:

-  Install `swiFTP.`_
-  Run it, start your server.
-  Use **nautilus** to connect to the server and move your files or the
   **ftp command** (man ftp) to send your files.
-  That's all!

Notes:

-  Tomdroid is only a read only client now.
-  I'm not sure if Tomdroid even updates notes. You may have to delete
   all application data for Tomdroid before a fresh sync.
-  I haven't found a way to pin point what notes need to be copied.
   Their file names aren't based on the name of the note. I'm still
   looking for a way to do this. When I copy my notes now, I also
   happened to copy the templates.

.. _using Gnote to unclutter one's daily note: http://fedoraproject.org/en/using/tutorials/gnote.html
.. _Gnote: https://live.gnome.org/Gnote
.. _Tomdroid: https://launchpad.net/tomdroid
.. _swiFTP.: http://code.google.com/p/swiftp/

