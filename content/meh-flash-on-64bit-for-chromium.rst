meh... flash on 64bit , for chromium
####################################
:date: 2010-07-08 11:36
:author: ankur
:category: Tech
:tags: Fedora
:slug: meh-flash-on-64bit-for-chromium

There's an ongoing `discussion on 64bit flash on the fedora-test list`_.
I learnt that Adobe had yanked the 64bit flash plugin (***I call it
"meh!!", and it will be henceforth referred to as "meh!!" in this
post***). I went back to the `fedora flash page on the wiki`_ and
installed the nspluginwrapper etc. to fall back to the 32 bit version of
"meh!!". This works smoothly for FF, but didn't function on chromium.
The wiki has a section for chrome, but that didn't work for chromium
either. Googling gave me `this`_, which does somewhat work. "Meh!!"
crashes at times, but that is expected, right? I haven't added this info
on to the wiki yet. Wasn't sure if it was permitted or if this method is
correct.

.. _discussion on 64bit flash on the fedora-test list: http://lists.fedoraproject.org/pipermail/test/2010-July/091889.html
.. _fedora flash page on the wiki: http://fedoraproject.org/wiki/Flash
.. _this: http://www.linuxquestions.org/questions/fedora-35/flash-for-chromium-64-bit-815403/#post4025861
