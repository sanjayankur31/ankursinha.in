Bringing together Gitter, IRC, and Slack channels in one place on Riot
#######################################################################
:slug: bringing-together-gitter-irc-and-slack-channels-in-one-place-on-riot
:date: 2017-07-12 13:55:17
:author: ankur
:category: Tech
:tags: Community, Computational neuroscience, Fedora, FlatPak, Free software, Gitter, Linux, Planet
:summary: Different teams use different platforms to communicate within themselves. When teams on different communication platforms want to collaborate, though - there's a bit of an issue. In this post, I document how one can setup channels on various platforms (Slack_, IRC_, Gitter_) and bring them all together on Riot_.


Let's not let our choice of platform limit us
----------------------------------------------

There are usually multiple platforms that provide similar functions. For instance, one can pick between Github_, GitLab_, and BitBucket_ for collaborative development interfaces, and one certainly should have the freedom to do so. Similarly, one can use different operating systems, web browsers, phones, etc etc etc. But, one must remember is that for a lot of us, these are simply means to an end - not the end themselves. They are tools that facilitate the completion of our goals. Different individuals or teams preferring different platforms should not hamper collaboration under any circumstances.

When it comes to communcation, different teams use different platforms. Some prefer e-mails - either private or using a mailing list. E-mails work well, but they're often overkill for simpler tasks. They're also not the best mode for quick collaborative development. This is where real-time chat comes in. Most open source communities maintain both mailing lists and chat infrastructure.

When it comes to chat platforms too, there are multiple options. IRC_, Gitter_, and Riot_ are designed to handle large communities and are therefore, usually preferred by open source communities. Slack_ seems to be preferred by smaller teams. There are others - Mattermost_, for example, but I haven't much experience with them.

Often, I've found people wary of hopping on to a different platform simply because it's too much work to set up yet another client that one must then also monitor. While this is understandable, it then has what I consider quite a major downside - limited communication amongst groups that are on different platforms. Fortunately, most platforms support bridges which lets the user connect them with other platforms.


Riot - bringing it all together in once place
----------------------------------------------

.. raw:: html

    <center>


.. image:: {static}/images/20170628-riot.png
    :alt: Using riot to access IRC, Slack, and Gitter
    :target: {static}/images/20170628-riot.png
    :width: 70%
    :class: text-center img-responsive pagination-centered

.. raw:: html

    </center>

Riot_ is an Open source platform that uses the Matrix_ protocol. It's similar to IRC_, but it's a lot more usable. and what is better, one can integrate IRC_, Slack_, and Gitter_ into Riot_ - so one can interact with users over all these platforms in one place. For example, the image below shows `Neuroscience-central/Lobby <https://riot.im/app/#/room/%23neuroscience-central-lobby:matrix.org>`__ room  that I've set up on Riot_. But, I've also gone ahead and connected this room to the `Neuroscience-central/Lobby room on Gitter <https://gitter.im/neuroscience-central/Lobby>`__, and to the `#neuroscience-central-lobby channel on IRC <https://webchat.freenode.net/?channels=#neuroscience-central-lobby>`__. So, everyone on any of these platforms can communicate with each other.


.. raw:: html

    <center>


.. image:: {static}/images/20170628-riot-gitter.png
    :alt: Neuroscience-Central/Lobby on Riot integrated with the same room on Gitter.
    :target: {static}/images/20170628-riot-gitter.png
    :width: 70%
    :class: text-center img-responsive pagination-centered

.. raw:: html

    </center>


Setting up the integrations is rather easy too. One needs to go to the integrations tab and set them up.

.. raw:: html

    <center>


.. image:: {static}/images/20170628-riot-integrations.png
    :alt: Integrations on Riot
    :target: {static}/images/20170628-riot-integrations.png
    :width: 70%
    :class: text-center img-responsive pagination-centered

.. raw:: html

    </center>

There are `desktop clients <https://riot.im/desktop.html>`__ available for Riot_ too. (`Here's a COPR for Fedora <https://copr.fedorainfracloud.org/coprs/taw/Riot/>`__). `Here's a great post on opensource.com <https://opensource.com/article/17/5/introducing-riot-IRC>`__ discussing Riot_.

So, if you're an admin looking to set up a new chat channel - consider setting up on different platforms and integrating them with Riot_ - it'll make things a lot easier for your users.


.. _IRC: https://en.wikipedia.org/wiki/Internet_Relay_Chat
.. _Gitter: https://gitter.im
.. _Slack: https://slack.com
.. _Polari: https://wiki.gnome.org/Apps/Polari
.. _Irssi: https://irssi.org/
.. _HexChat: https://hexchat.github.io/
.. _Github: https://github.com
.. _Colloquy: http://colloquy.info/
.. _Riot: https://riot.im
.. _Matrix: https://matrix.org/
.. _Github: https://github.com
.. _BitBucket: https://bitbucket.com
.. _GitLab: https://gitlab.com
.. _Mattermost: https://mattermost.com
