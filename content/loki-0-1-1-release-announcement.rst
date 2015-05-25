loki-0.1.1 release announcement
###############################
:date: 2010-06-20 13:13
:author: ankur
:category: Tech
:tags: Fedora
:slug: loki-0-1-1-release-announcement

We had shortly discussed an app that notifies the user of a new comic
strip at the recent FAD. I got down to it last week and have come up
with a release. I call it `"loki"`_. It's really raw right now. It uses
libcurl and libconfig to read from a conf file and check for the
availability of a new comic strip. It does this by comparing the stored
previous issue time stamp with the "Last-modified" tag of the HTTP
header returned by the site's rss feed.

I haven't incorporated the notification area pop up and auto checking
yet. Its on my TODO list for the next release.

The app is "Autotoolized". Thanks `Siddhesh`_ for the workshop and links
later to get me started.

The sources are available `here`_.

Feedback is welcome. In fact feedback is REQUIRED ;)

Comics it currently looks at:

#. `xkcd`_
#. `achewood`_
#. `A softer world`_
#. `Butter cup festival`_
#. `Dinosaur comics`_
#. `Indexed`_
#. `The perry bible fellowship`_
#. `Questionable Content`_
#. `Wondermark`_

You can make changes to the config files in ~/.loki to
add/enable/disable/remove comics.

.. _"loki": en.wikipedia.org/wiki/Loki
.. _Siddhesh: https://fedoraproject.org/wiki/User:Siddhesh
.. _here: http://ankursinha.fedorapeople.org/loki
.. _xkcd: http://www.xkcd.com
.. _achewood: http://achewood.com
.. _A softer world: http://www.asofterworld.com/
.. _Butter cup festival: http://www.buttercupfestival.com/index.htm
.. _Dinosaur comics: http://www.qwantz.com/index.php
.. _Indexed: http://thisisindexed.com
.. _The perry bible fellowship: http://pbfcomics.com
.. _Questionable Content: http://questionablecontent.net/
.. _Wondermark: http://wondermark.com/
