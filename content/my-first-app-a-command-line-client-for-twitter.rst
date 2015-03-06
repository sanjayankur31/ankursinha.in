My first app : A command line client for twitter
################################################
:date: 2009-05-14 08:59
:author: ankur
:category: Tech
:tags: C, command line client, curl-devel, libxml2, ncurses, twitter
:slug: my-first-app-a-command-line-client-for-twitter

I've been coding in C for sometime. Been working on a command line app
for twitter (I couldn't find one). I've made something and it barely
works. It's under heavy development (whatever I keep doing with it all
day that is).

Currently, it **sends,receives updates,replies to them and retweets**.
Really a bare minimum. I'm working on it , learning a lot of new things
in the process, and hope to make it a full fledged twitter client for
terminal lovers such as me. It uses libcurl,ncurses,libxml2.

It's available `here`_. It's not even an Alpha. I call it the
"bare-just-works" release. It doesn't break systems, if that's what
youre thinking. Please give it a try and provide feedback at *sanjay DOT
ankur AT gmail DOT com*. If you have the time to go through the source
and can advise me on better ways of implementing what I've done, please
do. I'm still a novice!

It still doesn't have Unicode support. I'm learning how to implement
that in C and it's on the "To-do" list. Please read through the README
before trying it.

|Screenshot|\ Screenshot

.. _here: http://ankursinha.fedorapeople.org/twit_tui/twitter_tui.tar.bz2

.. |Screenshot| image:: http://dodoincfedora.files.wordpress.com/2009/05/screenshot-ankurankur-documents-programs-twitui-twitter_tui1.png
   :target: http://ankursinha.fedorapeople.org/twit_tui/2.png
