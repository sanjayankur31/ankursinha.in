[How to] set up your Pelican based static blog
##############################################

:date: 2015-03-02 10:39
:tags: Pelican, Wordpress
:category: Tech
:slug: howto-pelican
:author: ankur
:lang: en
:summary: A quick note on how you can set up a static blog like mine using Pelican.

In my last post, I mentioned that I had moved to a Pelican based blog. In this post, I'll document how I did this, for myself as a future reference and for others that might be looking for a resource. **Yet another howto**.

Requirements
------------

- I'm using a Fedora_ system, but you can use another Linux (or not) distribution too. Pelican is written in Python, so it should be easily usable on any system that has Python on it. This guide will limit itself to Fedora.

- Pelican is available in the Fedora repositories:

    .. code-block:: bash

        sudo yum install python-pelican

- Git and a Github_ account

- Your favourite text editor

- Your hosting space - of course

Steps
-----

- Create a new repository on github and clone it. This will hold the source files for your posts.

- To create a skeleton file, you can use the `pelican-quickstart` command.

- This sets up your directory structure, like this:

    .. code-block:: console

        $ tree -L 1
        .
        ├── content
        ├── develop_server.sh
        ├── fabfile.py
        ├── Makefile
        ├── output
        ├── pelicanconf.py
        ├── pelican-plugins
        ├── publishconf.py
        ├── README.md
        └── voidy-bootstrap

The content directory will contain the source files. You can either use rst_ or markdown_ to write them. The output directory will contain the files pelican generates. The readme file is one that you'll set up, just for your github repo. voidy-boostrap is a theme I'm using and pelican-plugins is the plugins repository. More on these later.

- All you need to do is write a hello world post. Something like this:

    .. code-block:: rst

        Hello World
        ###########

        :date: 2015-03-02 10:39
        :tags: Pelican, Wordpress
        :category: Tech
        :slug: hello-world
        :author: ankur
        :lang: en

        Hello World!

- To *compile* this, you run `make html` and then `make serve` to take a look at your post (Direct your browser to `localhost:8000`). By default, it'll look quite simple. You can use pelican-themes_ to change how your stuff looks. They also have a set of plugins_ you can use.

Importing from Wordpress
------------------------

- Pelican `provides a tool`_ that lets you import your wordpress blog into it: `pelican-import`. It's far from perfect, though, so you're probably going to need to work on your posts before you publish. `sed is quite useful`.

References
----------

More links that you can look at:

- http://docs.getpelican.com/en/latest/content.html
- http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
- http://pygments.org/docs/formatters/
- http://docs.getpelican.com/en/latest/quickstart.html 

Anyway, have fun with it - my blog now is blazing quick!

.. _Fedora: http://fedoraproject.org 
.. _Github: http://github.com
.. _rst: http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. _markdown: http://daringfireball.net/projects/markdown/syntax
.. _pelican-themes: https://github.com/getpelican/pelican-themes
.. _provides a tool: http://docs.getpelican.com/en/3.5.0/importer.html
.. _sed is quite useful: http://www.grymoire.com/Unix/Sed.html
.. _plugins: https://github.com/getpelican/pelican-plugins
