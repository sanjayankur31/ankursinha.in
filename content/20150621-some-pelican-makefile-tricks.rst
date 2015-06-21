Some Pelican tricks
###################
:date: 2015-06-21 01:03:35
:author: ankur
:category: Tech
:tags: Bash, Blog, Pelican, Vim, Fedora
:slug: some-pelican-makefile-tricks
:summary: Some tricks I thought up last night to improve my Pelican based blogging work flow.

Pelican_ is pretty brilliant, as I've already said in `posts before`_. Recently, I was well, plain bored, decided to see if I can make my blogging workflow any more efficient. What's better than some tinkering to use up some time, eh?

Adding new posts using a Makefile
---------------------------------
This one is in the `Pelican tips and tricks page`_ but I've modified it a little to suit my needs. I use `restructured text`_ to write my posts, and the Makefile improvements on the tricks page seem to be for markdown_ users anyway. This is what I've added to `my Makefile`_:

.. code-block:: makefile

    DATE := $(shell date +'%Y-%m-%d %H:%M:%S')
    DATEYYMMDD := $(shell date +'%Y%m%d')
    SLUG := $(shell echo '${NAME}' | sed -e 's/[^[:alnum:]]/-/g' | tr -s '-' | tr A-Z a-z)
    EXT ?= rst
    newpost:
    ifdef NAME
        git checkout -b $(DATEYYMMDD)-$(SLUG)
        echo "$(NAME)" >  $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
        echo -n "$(NAME)" | sed "s/./#/g" >>  $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
        echo >>  $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
        echo ":date: $(DATE)" >> $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
        echo ":author: ankur" >> $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
        echo ":category: " >> $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
        echo ":tags: " >> $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
        echo ":slug: $(SLUG)" >> $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
        echo ":status: draft" >> $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
        echo ":summary: " >> $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
        echo ""              >> $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
        echo ""              >> $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
        ${EDITOR} ${INPUTDIR}/$(DATEYYMMDD)-${SLUG}.${EXT}
    else
        @echo 'Variable NAME is not defined.'
        @echo 'Do make newpost NAME='"'"'Post Name'"'"
    endif

    editpost:
    ifdef NAME
        ${EDITOR} ${INPUTDIR}/$(DATEYYMMDD)-${SLUG}.${EXT}
    else
        @echo 'Variable NAME is not defined.'
        @echo 'Do make editpost NAME='"'"'Post Name'"'"
    endif

    newpage:
    ifdef NAME
        echo "Title: $(NAME)" >  $(PAGESDIR)/$(SLUG).$(EXT)
        echo "Slug: $(SLUG)" >> $(PAGESDIR)/$(SLUG).$(EXT)
        echo ""              >> $(PAGESDIR)/$(SLUG).$(EXT)
        echo ""              >> $(PAGESDIR)/$(SLUG).$(EXT)
        ${EDITOR} ${PAGESDIR}/${SLUG}.$(EXT)
    else
        @echo 'Variable NAME is not defined.'
        @echo 'Do make newpage NAME='"'"'Page Name'"'"
    endif

    editpage:
    ifdef NAME
        ${EDITOR} ${PAGESDIR}/${SLUG}.$(EXT)
    else
        @echo 'Variable NAME is not defined.'
        @echo 'Do make editpage NAME='"'"'Page Name'"'"
    endif

It's quite simple really. It adds a new "newpost" command to the Makefile. When you run something like this:

.. code-block:: bash

    make newpost NAME="trying out a new pelican makefile"

It just creates a new post/page file in your contents directory. I don't think I'll ever use the edit functionality to be honest, but I saw no harm in letting it stay in the Makefile. Since I use Git to manage my sources, I threw in a command that creates a new branch for each post too. There's so much more you can do, obviously.

Vim commands to quickly get your tag and category list
-------------------------------------------------------

An issue I recently had with Pelican is what I call "tag explosion" - I couldn't keep track of what tags I was using. This is easier to manage with Wordpress which gives you a list to choose from. Similarly, in Pelican, each post should belong to a particular category. Generally, I open my site and look up this info, but that's a bit tedious. I thought up a workaround for Vim - add these to your ~/.vimrc:

.. code-block:: vim

    " some pelican helpers
    command! GetCategoryList :read !grep -o -h '^:category:.*' content/*rst  | sed 's/:category: //' | tr ',' '\n' | sed 's/^[[:space:]]*//' | sort | uniq | sed '/^[[:space:]]*$/ d' | tr '\n' ',' | sed 's/,/, /g' | sed 's/,[[:space:]]*$//'
    command! GetTagList :read !grep -o -h '^:tags:.*' content/*rst  | sed 's/:tags: //' | tr ',' '\n' | sed 's/^[[:space:]]*//' | sort | uniq | sed '/^[[:space:]]*$/ d' | tr '\n' ',' | sed 's/,/, /g' | sed 's/,[[:space:]]*$//'


This adds two commands - GetCategoryList and GetTagList which print the lists in your Vim buffer. You can then choose which ones you want - use something like `df,` to get rid of ones you don't and so on.

These two have made my writing work flow a bit better, but I know I'll find more things to tinker and optimise in the future.
Anyway, happy writing!

.. _posts before: http://ankursinha.in/blog/tag/pelican/
.. _Pelican tips and tricks page: https://github.com/getpelican/pelican/wiki/Tips-n-Tricks
.. _restructured text: http://docutils.sourceforge.net/rst.html
.. _markdown: http://daringfireball.net/projects/markdown/
.. _my Makefile: https://github.com/sanjayankur31/ankursinha.in/blob/master/Makefile
.. _Pelican: http://blog.getpelican.com/
