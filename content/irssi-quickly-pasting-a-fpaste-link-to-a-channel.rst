irssi : quickly pasting an fpaste link to a channel
###################################################
:date: 2010-12-03 18:21
:author: ankur
:category: Tech
:tags: Fedora
:slug: irssi-quickly-pasting-a-fpaste-link-to-a-channel

I recently posted my\ `list of irssi aliases`_ that come handy on the
`fedora IRC channels`_. Today, I was experimenting and found something
new. Suppose you head into **#fedora**, and ask for help. Someone asks
you to **fpaste** something, lets say :

::

    $ lsusb | fpaste

Now, instead of changing to another terminal tab, or another screen
window to do this, all you need to do is this :

::

     /exec -m #fedora lsusb | fpaste

Yes, that's it! And in #fedora, the **result**\ is an awesome:

::

    18:05 < FranciscoD> Uploading (0.7K)...
    18:06 < FranciscoD> http://fpaste.org/WUxU/

Saves time and is more convenient. Cheers!

EDIT: Some more digging, and we have an improved command:

::

    /exec -m #fedora echo -n "NICK: "; lsusb | fpaste 2>&1 | grep "fpaste" 

This sends the link to the respective NICK, and only one line, the link,
since it's been grepped.

Aliases for irssi :

::

     
    /alias fedoraFpasteResult /exec -m #fedora echo -n "$0: "; $1- | fpaste 2>&1 | grep "fpaste"

    /alias fedoraFpasteResultGeneral /exec -m $0 echo -n "$1: "; $2- | fpaste 2>&1 | grep "fpaste"

.. _list of irssi aliases: http://dodoincfedora.wordpress.com/2010/11/29/some-troubleshooting-links/
.. _fedora IRC channels: http://fedoraproject.org/wiki/Communicate#User_Help
