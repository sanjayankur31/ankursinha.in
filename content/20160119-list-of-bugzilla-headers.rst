List of bugzilla headers
########################
:date: 2016-01-19 14:03:29
:author: ankur
:category: Tech
:tags: Fedora, Bugzilla, Community, GNOME
:slug: list-of-bugzilla-headers
:summary: A list of headers that the RedHat bugzilla includes in e-mails that it sends.

The RedHat bugzilla instance that the Fedora community uses includes lots of helpful e-mail headers in its communications. These can be parsed by different e-mail clients such as Evolution to give us more information about a bug notification. People have mentioned these from time to time on the Fedora mailing lists. I wanted to configure Evolution to show them too, but I could neither find the mails on the mailing list nor a reference document in `bugzilla's documentation <https://cse.google.com/cse?cx=008043952663535741821%3A9whwb87ip5a&q=headers#gsc.tab=0&gsc.q=headers&gsc.page=1>`__. I saved one of my e-mails to mbox and got the list out that way. Here it is, in case you were looking too:


.. code:: python

    X-Bugzilla-Type: changed
    X-Bugzilla-Watch-Reason: None
    X-Bugzilla-Classification: Fedora
    X-Bugzilla-Product: Fedora
    X-Bugzilla-Component: <usually a package name>
    X-Bugzilla-Sub-Component: 
    X-Bugzilla-Version: <Fedora version>
    X-Bugzilla-Keywords: 
    X-Bugzilla-Severity: unspecified
    X-Bugzilla-Who: <some email>
    X-Bugzilla-Status: ASSIGNED
    X-Bugzilla-Priority: unspecified
    X-Bugzilla-Assigned-To: <some email>
    X-Bugzilla-Target-Milestone: ---
    X-Bugzilla-Changed-Fields: 
    X-Bugzilla-Comment: public
    X-Bugzilla-Reporter: <some email>

I've added a few comments to explain what the headers are. In Evolution, you'd go to **Edit > Preferences > Mail Preferences > Headers** and add the headers you want to see to the list there.

Cheers!

PS: If you do find a reference list someplace in the documentation, please do let me know.
