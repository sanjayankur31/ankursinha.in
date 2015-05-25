The 406 error conundrum!
########################
:date: 2013-08-30 13:34
:author: ankur
:category: Tech
:tags: Fedora
:slug: the-406-error-conundrum

Some of you may have noticed that my blog wasn't coming up on the planet
recently. No? \*sigh\*. Well, **Ralph(threebean)** finally dug out the
"bug" earlier today. The first clue was the error from the planet that
**Kevin** was nice enough to get for us:

``ERROR:planet.runner:Error 406 while updating feed http://ankursinha.in/wp/category/fedora/feed/``

Unfortunately, the `406 error description`_ doesn't tell us much. What
it did tell us though was that there's some incoherence in the header
that our planet instance sends and the reply it receives. We kept trying
other clients (curl/wget) and the default python http request and could
not replicate it. After a lot of digging, Ralph ended up looking at bare
httplib2 code since planet uses httplib2 to make it's requests. When he
tried to get the blog feed off httplib2, he ran into this:

`` >>> import httplib2 >>> h = httplib2.Http() >>> response, content = h.request("http://ankursinha.in/wp/feed/") >>> response.status 406 >>> response, content = h.request("http://ankursinha.in/wp/feed/", headers={'user-agent': 'trololololololol 9000'}) >>> response.status 200``

It appears that mod\_security, or waf (web app firewalls) `tend to deny
access to a list of agents`_ as **athmane** explained later in
``#fedora-noc``. The current work around is to just change the agent
that the planet instance uses, which Ralph already did.

It wasn't really a major bug, but it was sure a tricky one to triage. If
your blog wasn't turning up on the planet because of a 406 error, this
should've hopefully fixed it. Cheers!

.. _406 error description: http://www.checkupdown.com/status/E406.html
.. _tend to deny access to a list of agents: https://github.com/SpiderLabs/owasp-modsecurity-crs/blob/master/base_rules/modsecurity_35_scanners.data
