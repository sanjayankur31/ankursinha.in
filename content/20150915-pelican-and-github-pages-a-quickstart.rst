Pelican and github pages - a quickstart
########################################
:date: 2015-09-15 17:53:08
:author: ankur
:category: Tech
:tags: Fedora, Pelican, Programming, Social
:slug: pelican-and-github-pages-a-quickstart
:summary: A quick post on how to get started with Pelican using Github pages.


A **really** quick howto !

Set up a github.io page
------------------------

To create your github user page, head over to github and create two new repositories - username.github.io-src and username.github.io - `as explained here`_. The src repository will hold the sources of your blog and the username.github.io repository will contain the output html files that pelican generates. Since we're going to add the output directory as a submodule, **initialise it with a readme** - I can't seem to add a bare git repository as a submodule in a simple way.

Install Pelican
---------------

On Fedora, this is a very very simple command:

.. code:: bash

    sudo dnf install python-pelican

If you aren't on a Fedora system, you'll have to install these packages another way, like with `pip`. I'd suggest using a virtualenv, but it's up to you:

.. code:: bash

    virtualenv blog_virt
    cd blog_virt
    source bin/activate

    pip install pelican ghp-import #then change to your git repository and continue

Set up the blog with pelican
-----------------------------

Pelican provides an excellent quickstart command. Double check that you're working in the source git repository using:

.. code:: bash

    git remote -v

Then, clone the output repository as a git submodule:

.. code:: bash

    git submodule add git@github.com:sanjayankur31/sanjayankur31.github.io.git output #replace the URL with the correct one.

Then, run:

.. code:: bash

    pelican-quickstart

It'll ask you various questions, just answer them. If you're using the latest version of Pelican, it'll ask you if you want to use github pages and so on.

Open the `publishconf.py` file and set the `DELETE_OUTPUT_DIRECTORY` variable to False. Otherwise, each time you publish, it deletes your submodule - we don't want that.

Tweaks
-------

There are various `tweaks and tips`_ mentioned here that you should look at. One of the more handy ones is the addition of a newpost command in the Makefile. 

First post
-----------

`Write a quick post`_!!

Build, commit, push, and you're done!
-------------------------------------

Once done, you build your blog and check if everything is OK:

.. code:: bash

    make html; make serve #creates a demo site and serves it on localhost:8000

This runs a local webserver on port 8000 - `direct your browser there`_ to see the results of your work!
If everything is OK, generate the website, add your files, commit them, and push to your repositories:

.. code:: bash

    make publish #creates the complete site

    # Commit to the output submodule first
    cd output
    git add .
    git commit -m "First post."
    git push -u origin master

    # The commit the source repository
    cd ..
    echo '*.pyc' >> .gitignore #don't need pyc files
    git add .
    git commit -m "First commit."
    git push -u origin master
    # Sources committed


That's all! Head over the username.github.io and see the new site you've just created!

Caveats and customisations
---------------------------

Everything can be pretty much customised in Pelican. To start with, there are `a set of themes that you can choose from`_. On top of that, you even have `a set of plug-ins`_ that help you add various functionalities to your site. Of course, you can write your own or customise existing plugins and themes.

There's a tool called ghp-pages that the pelican documentation refers to, but as of Pelican 3.6.3 which Fedora 22 features, the tool doesn't work as described in the documentation. It's why I used the submodule method.

.. _as explained here: https://pages.github.com/
.. _tweaks and tips: https://github.com/getpelican/pelican/wiki/Tips-n-Tricks
.. _Write a quick post: http://docs.getpelican.com/en/3.6.3/content.html
.. _direct your browser there: http://localhost:8000
.. _a set of themes that you can choose from: http://pelicanthemes.com
.. _a set of plug-ins: https://github.com/getpelican/pelican-plugins
