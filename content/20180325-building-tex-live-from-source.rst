Building TeX Live from source
#############################
:date: 2018-03-25 18:15:05
:author: ankur
:category: Tech
:tags: TeX, Fedora
:slug: building-tex-live-from-source
:summary: I thought it'd be fun to try and build `TeX Live`_ from sources. So,
          I spent a day trying to do it. Here's how it went.


Between all the LaTeX_ vs Word_ discussions that I frequently become a part of,
is the beauty of how it all works. They're both marvels, even if they each take
turns to exasperate users. There are pros and cons of each, and each has their
learning curves.

I use LaTeX_ for various reasons. To start with, it takes me 5 minutes to write
a document in LaTeX_ and 30 to write the same in Word_, but it can be the
opposite for another user. May be I've gotten a system set up now where writing
in LaTeX_ isn't inefficient any more. This is me using Vim_, with `plugins
<https://github.com/sanjayankur31/vimfiles>`__.

Of course, the fact that it is `Free software
<https://tug.org/texlive/copying.html>`__ is very important to me. It may not
mean much to larger universities that have Microsoft services, but it does make
a difference to universities that don't have that kind of funding. When I'd
done my undergraduate degree back in India, for example, we didn't have a
university wide Microsoft license. I used Fedora_ throughout, and having `TeX
Live`_ (and other free software) available to me was quite something. We
must remember to think of the way events and actions impact society, or that's
my point of view, anyway.


Fedora_ provides `TeX Live`_ in its repos. It takes quite an effort to build it
since it's a whole bunch of packages that must be built. There's a bit of
scripting required to even `build the spec file
<https://src.fedoraproject.org/rpms/texlive/tree/master>`__. So, it's simply:

.. code:: bash

    sudo dnf install texlive

The advantage of the rpm packaging is that subsequent packages can also be
installed by specifying the :code:`sty` files. For the :code:`lineno` package,
for example, one can use:

.. code:: bash

    sudo dnf install 'tex(lineno.sty)'


Not everyone must build `TeX Live`_ from source, upstream provides binaries for
all platforms, and a `convenient installer
<https://www.tug.org/texlive/acquire-netinstall.html>`__.

.. image:: {static}/images/20180325-texlive.png
    :alt: TeX Live installer
    :target: {static}/images/20180325-texlive.png
    :width: 80%
    :class: text-center img-responsive pagination-centered


As it says, the whole collection is quite large, about 5GB.

Building from source
--------------------

I followed the `documentation
<https://www.tug.org/texlive/doc/tlbuild.html>`__ that's provided for this
already. Luckily, it uses Autotools_, and I've quite a bit of experience with
them. Fedora_ provides the 2016 release, so I played with the 2017 release
here. I also referred to the Fedora_ spec files, which made life so much easier:

- https://src.fedoraproject.org/rpms/texlive/blob/master/f/texlive.spec
- https://src.fedoraproject.org/rpms/texlive-base/blob/master/f/texlive-base.spec

The build turned out to be quite simple. Fetch the sources, and then run
:code:`configure && make && sudo make install`, and that's quite it for the
base packages.

I ran it on my headless `Fedora Server <https://getfedora.org/en/server/>`__
system, and it pretty much went off without a hitch. I now have a base `TeX
Live`_ distribution there in :code:`/usr/local/texmf-dist`. Note, that this
isn't sufficient. It only installs the basic bits of `TeX Live`_, not even the
LaTeX_ macro package. So, while it's easy and somewhat fun to tinker with on a
day off, I wouldn't suggest it for any end-users. On my work machines, the two
`Fedora Workstation <https://getfedora.org/en/workstation/>`__ installs, I'm
going to stick to the Fedora_ packages, which are more than sufficient! (If
you're a Fedora_ user, please shower the Fedora_ `TeX Live`_ maintainers with
`cookies <http://threebean.org/blog/karma-cookies/>`__! Get on `#fedora-devel
<https://webchat.freenode.net/?channels=#fedora-devel>`__ on Freenode, and go
:code:`<FAS username/Linked IRC nick>++`)


.. _Autotools: http://www.gnu.org/software/automake/manual/html_node/Autotools-Introduction.html#Autotools-Introduction
.. _Vim: https://www.vim.org
.. _Fedora: https://fedoraproject.org
.. _TeX Live: https://www.tug.org/texlive/
.. _LaTeX: https://ctan.org/pkg/latex
.. _Word: https://en.wikipedia.org/wiki/Microsoft_Word
.. _CTAN: https://ctan.org/
