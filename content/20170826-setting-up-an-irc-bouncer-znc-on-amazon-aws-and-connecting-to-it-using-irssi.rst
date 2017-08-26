Setting up an IRC bouncer (ZNC) on Amazon AWS and connecting to it using Irssi
##############################################################################
:date: 2017-08-26 13:42:40
:author: ankur
:category: Tech
:tags: Fedora, IRC, ZNC, AWS, Irssi
:slug: setting-up-an-irc-bouncer-znc-on-amazon-aws-and-connecting-to-it-using-irssi
:summary: I finally found the time to set up an IRC bouncer to keep myself permanently connected to IRC_ networks. This post documents how I went about it using `Amazon AWS`_, ZNC_, and Irssi_.

Given how important a collaborative tool the IRC_ is for us free software enthusiasts, it is imperative that one be accessible on various networks as much as possible. Personally, I used to leave my system at the laboratory logged in all the time, but then I'd have to VPN into the university and then SSH into my system there. Not ideal, really.

The commonest way of always remaining connected to the IRC_ is to use an IRC_ bouncer. The bouncer remains connected to one's networks all the time, and one can use a client from wherever to connect to the networks via this bouncer. There are a few free to use bouncers that one can use, of course. On preliminary investigation though, it didn't seem too hard to set a private instance up, so I gave it a go.

Amazon AWS set up
=================

The bouncer must be deployed on a system that is accessible from anywhere to be truly useful. While I do have hosting for this blog, it's cheap shared hosting without shell access. So, I needed another machine. Some research led me to `the free tier on Amazon AWS <https://aws.amazon.com/free/>`__ where one can get a free AWS instance for 12 months. The process is `very well documented <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/>`__, so I won't clone it here. There are various Linux operating systems that one can choose from. Being a Fedora user, I opted for Red Hat Enterprise Linux, but any Linux would work.

After the AWS instance is up and running, one must follow the instructions in the documentation to enable SSH access to it. It requires setting up security rules using the web console.

ZNC set up
==========

There are a few bouncers available. I chose the popular ZNC_ bouncer. 

On a Red Hat system, ZNC_ is available in the `"extra packages" repositories <https://fedoraproject.org/wiki/EPEL#How_can_I_use_these_extra_packages.3F>`__. So, it comes down to a few commands:

.. code:: bash

    sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm 
    sudo yum install znc

This will install the ZNC_ package. ZNC_ provides a `simple way of configuring <https://wiki.znc.in/Configuration>`__ it too:

.. code:: bash

    sudo znc --makeconfig


Of course, one must make sure that the service is always running:

.. code:: bash

    sudo systemctl enable znc.service
    sudo systemctl start znc.service

During the configuration, one must note what port ZNC_ was set up to listen to, and what the public IP of the AWS machine is.  These are required to set up the IRC_ client later, in this case Irssi_. One must also remember to open this port to inbound connections. This can be done using the AWS web console in the same way as the SSH port was enabled earlier. Please refer to the `relevant bits in the AWS documentation <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html>`__. ZNC_ can be further configured through the `web administration interface <https://wiki.znc.in/Webadmin>`__. One can add more networks, channels, and useful `ZNC modules <https://wiki.znc.in/Modules>`__ there.

`Browsers seem to ban connecting to a few ports that are deemed dangerous <https://jazzy.id.au/2012/08/23/why_does_chrome_consider_some_ports_unsafe.html>`__. I found this to be the case on Firefox_, Chrome_, and Qutebrowser_. Instructions on how to workaround this ban are here for `Firefox <https://support.mozilla.org/en-US/questions/1083282>`__ and `Chrome <https://superuser.com/questions/188006/how-to-fix-err-unsafe-port-error-on-chrome-when-browsing-to-unsafe-ports>`__ respectively. I couldn't figure out how this needs to be done for Qutebrowser_ and I've filed an `issue here <https://github.com/qutebrowser/qutebrowser/issues/2925#issuecomment-324812384>`__. It seems to be an `upstream QT issue <https://bugreports.qt.io/browse/QTBUG-62808>`__ that is already being looked into.

Irssi set up
============

Once the bouncer has been deployed correctly, all that remains is to configure an IRC_ client to connect to it. I use Irssi_ myself so the steps documented here will be specific to it. However, they should be general enough to be applicable to other clients too.

Installing Irssi_ on a Fedora system is trivial, of course:

.. code:: bash

    sudo dnf install Fedora # node that Fedora uses DNF now

Irssi_ reads its configuration file from :code:`~/.irssi/config`. There are commands to configure servers, and these write to the configuration file that has quite a simple structure and can be edited directly using a text editor. The relevant snippets from my configuration file are below. Here, because we're connecting to our IRC_ servers via the bouncer, the address in use will be that of the bouncer. The ZNC_ web administration interface informs on what the password should be.

.. code:: text

    servers = (
      {
        address = "<public address of the AWS instance";
        chatnet = "freenode";
        port = "<port ZNC is listening to>";
        password = "<ZNC username/network1:password>";
        use_tls = "yes";
        tls_verify = "no";
        autoconnect = "yes";
      },
      {
        address = "<public address of the AWS instance";
        chatnet = "slack";
        port = "port ZNC is listening to";
        password = "<ZNC username/network2:password>";
        use_tls = "yes";
        tls_verify = "no";
        autoconnect = "yes";
      }
    );


Irssi_ can also be customised to suit the user - such as the window layout, plug-ins, theme. I won't document how here. Instead I refer to the `Irssi documentation <https://irssi.org/documentation/>`__.

Conclusion
==========

That's quite it. The bouncer will always run, and wherever one is, one can use a client to keep up with happenings. I hope this post will make it easier for others to set up their private bouncers too. Comments, and feedback are always welcome. Cheers!


.. _IRC: https://en.wikipedia.org/wiki/Internet_Relay_Chat
.. _Amazon AWS: https://aws.amazon.com
.. _ZNC: https://znc.in
.. _Irssi: https://irssi.org/
.. _Firefox: https://www.mozilla.org/en-GB/firefox/new/
.. _Chrome: https://www.google.com/chrome/index.html
.. _Qutebrowser: https://www.qutebrowser.org/
