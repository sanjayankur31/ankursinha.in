Fedora free-media tool: making modifications to the trac?
#########################################################
:date: 2012-02-17 12:28
:author: ankur
:category: Tech
:tags: Fedora
:slug: fedora-free-media-tool-making-modifications-to-the-trac

I got a feature request for the `free-media tool`_ that I've been
working on. `Benedikt Schäfer`_ asked me if resolving a ticket in the
tool could also change the ticket status on the trac. While this is on
the TODO already, I sat up last night and looked into it.

I'm making use of cURLpp, which is just a C++ wrapper around libcURL for
the tool. Getting the report wasn't really complex:

#. Log in and save auth cookie
#. Use saved auth and get report

It seems making modifications is way more complex. I am required to POST
data to the server. The complexity is because of the numerous POST
fields that I need to first GET, modify (manually here) and then POST
back to the server. Here's what the POST data looks like: (I used the
`firefox tamperdata add-on`_ to get this info. Great add on!)

    \_\_FORM\_TOKEN=xxxxxxxxxxxxxxxxxx&comment=&field\_summary=Test&field\_version=i386+DVD&field\_keywords=&field\_blockedby=&field\_blocking=&field\_email=&field\_country=&action=resolve&action\_resolve\_resolve\_resolution=fixed&ts=&replyto=&cnum=8&submit=Submit+changes

The \_\_FORM\_TOKEN needs to be extracted from the cookie the server
sends. The rest are values I need to get from the ticket. To make any
changes, I need to modify the action, comment, cnum etc fields. I spent
about three hours tussling with cURL trying to successfully make a
modification, and.. failed :/ (I've never been a web dev really, so it
could just be that).

Would anyone know how I could get this done? I've looked around for a
TRAC API which would've made life much simpler, but I haven't really
found anything. Any and all help would be appreciated :)

.. _free-media tool: http://dodoincfedora.wordpress.com/2012/02/16/fedora-free-media-tool-version-0-2alpha/
.. _Benedikt Schäfer: http://fedoraproject.org/wiki/User:Ib54003
.. _firefox tamperdata add-on: https://addons.mozilla.org/en-US/firefox/addon/tamper-data/
