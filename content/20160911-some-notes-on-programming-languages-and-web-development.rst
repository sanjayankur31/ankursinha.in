Some notes on programming languages and web development
#######################################################
:date: 2016-09-11 20:58:54
:author: ankur
:category: Tech 
:tags: Fedora, Programming, Python, Erlang, Rust, Flask, RoR, Scala
:slug: some-notes-on-programming-languages-and-web-development
:summary: Just some notes on different programming languages that one can use for web development. Includes Python, RoR, Rust, Erlang?

Even before I begin, I must state that I'm not a web developer. I've never been one, and I have no intention to turn into one either. It isn't that I don't like developing web applications. On the contrary, I find the topic incredibly interesting. It's just that everything I need has pretty much already been developed by web developers, so I've never had to write an app myself. Add to that my lack of interest in pursuing a career the software development industry - I prefer my research - the implications are that I will always prioritise research related development.

Take this blog, for example. It once used to be a `Wordpress <https://wordpress.org/>`__ deployment, but I eventually got fed up with it bleeding the resources of my shared hosting space and moved to a static site. I didn't even bother learning a new language like `Ruby <https://www.ruby-lang.org/en/>`__ to use `Jekyll <https://jekyllrb.com/>`__. I found something that was written in `Python <https://www.python.org/>`__, a language that I know pretty well - `Pelican <http://docs.getpelican.com/en/3.6.3/>`__ - which works really well. So, really, for my web requirements, I tend to pick the path of least effort.

Recently though, a requirement has arisen. I use Wikindx_ as my bibliography manager. There are various desktop applications available, of course, but the advantage of a web application is that it's accessible from everywhere. `Mendeley <https://www.mendeley.com/features/>`__ is quite nice and so is `EndNote <https://en.wikipedia.org/wiki/EndNote>`__, but they aren't free software, so I shan't use them. Now, even though Wikindx_ is a good bibliography manager with lots of additional helpful features, I want something that can also keep up with new journals, and help me cut through the plethora of articles to find ones that are relevant to my work. I follow about 40 journals using `Liferea <https://lzone.de/liferea/>`__, but honestly, going through all of them, even with search folders, is a mammoth task. One option is to extend Wikindx_. Hrm, it's written in PHP - do I want to learn PHP? Not really - so that isn't really a solution. It'd be nice if I could use this as a constructive exercise, to learn something new, wouldn't it?

The obvious solution is to hack something up! I could write a bunch of scripts in some language quickly, but I'd prefer not to lose the functionality that I've gotten used to in Wikindx_. So, let's write a web application then! Yay!

Before I begin hacking left, right, and center, I wanted to decide what I want to learn. So I did a little research on the different languages that can be used for web development and their features and drawbacks. I'm not going to come up with a conclusion here. In fact, I'm not even going to discuss the strengths and weaknesses of the languages here. They have different designs, and work for different purposes. As long as I can build a web application with reasonable time and effort, I don't really care too much about the nitty-gritty details. I'm not going to waste time on another "this language is better than that one!" argument. All I'm going to do below is list the options I have.

To begin with, this is meant to be a fun exercise. So, I'm going to write it as a single user app - to reduce the amount I need to learn. When it's done and if my colleagues think it's worth developing into a complete multi user website with collaborative features, it can be extended. So, yea, a prototype to begin with.

My requirements:

- the learning curve must not be tedious nor boring - rather, it should be something fresh
- a framework would be nice - so that the task isn't too taxing
- good documentation is always welcome
- good community support is also welcome - sometimes you need someone to throw you an RTFM or LMGTFY link
- I don't reckon scalability is an issue at the moment?

Python
-------

The first on my list was obviously Python. I know the language well. I know the ninjas over at Fedora Infrastructure love Python - `Bodhi <https://bodhi.fedoraproject.org>`__ seems to use `Pyramid <http://www.pylonsproject.org/>`__, and `Pagure <https://pagure.io>`__ uses `Flask <http://flask.pocoo.org/>`__. Python is easy to use, and it's really quick to come up with a working prototype. These frameworks are also widely used, so there are enough resources for beginners to learn off - tutorials, cook books, and the sort.

However, I already know Python and while learning how to use a framework is interesting, learning a new language is probably more interesting?

Ruby
----

Ruby on Rails seems to be quite popular. Github and Twitter use it - as front ends, I seem to find. The framework is also quite widely used - people say lots of good stuff about it. Ruby seems like a good language to learn too. This looks promising.

NodeJS
------

Of course, this must be considered. It seems to be everywhere now. Javascript is quite simple, I've used it a bit. Maybe?

Go
--

Ah, a Google language. I see quite a few frameworks also available. The documentation seems to be decent too - maybe?

Rust
-----

This one looks kind of exciting. It's quite new, and isn't as widely used. The documentation may be an issue? I see a framework already - `Iron <https://github.com/iron/iron>`__.

Scala
------

Yes, it isn't Java, and it doesn't force you to use OOP, but it really doesn't look too interesting to me.

Erlang
------

Ah, now here's something new - a functional programming language! That's something I haven't used in a while. A nice framework with good documentation is here too - `ChicagoBoss <https://github.com/ChicagoBoss/ChicagoBoss>`__. `Some posts I've read <https://www.quora.com/Why-choose-Erlang-for-web-development>`__ also say that it's really quick compared to Go/Node.

So, what do I do?
-----------------

It's always quite hard to pick a new language for a general purpose that so many languages can fulfil. Usually, I'd pick a language that had a library that fit my requirements exactly. In the case of the above mentioned languages, I know very little about web development. So, I'm going to do what people that don't know much do - pick two arbitrarily! I think I'll start with Python/Flask to quickly get something working - it shouldn't take me more than a weekend. Then, once I have a working demo, I can look at replicating it in Erlang - learn a language quite different from the usual ones that I usually do?

Sounds like a plan ;)


.. _Wikindx: http://wikindx.sourceforge.net/features.html
