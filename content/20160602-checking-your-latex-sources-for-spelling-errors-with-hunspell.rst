Checking your LaTeX sources for spelling errors with Hunspell
#############################################################
:date: 2016-06-02 11:42:00
:author: ankur
:category: Research
:tags: Fedora, Git, LaTeX, Linux, Vim 
:slug: checking-your-latex-sources-for-spelling-errors-with-hunspell
:summary: For command line users that write in LaTeX_, Hunspell_ is a great tool to check spellings.

I usually use `Vim <http://www.vim.org/>`__ and a `Makefile <https://en.wikipedia.org/wiki/Makefile>`__ when writing LaTeX documents. Even though `Vim does permit you to check your spellings <http://vimdoc.sourceforge.net/htmldoc/spell.html>`__, it's always nice to run the entire text through a standalone spell checker before passing your documents on to others.


The workflow is quite simple. Once you've written your text, you commit your changes, and then you can use one of either Aspell_ or Hunspell_ to check your text for spelling errors. Both provide an interactive interface that makes them easy to use.

On `Fedora <http://getfedora.org>`__, you can install them using :code:`dnf`:

.. code:: bash

    sudo dnf install aspell hunspell

You'll also need to make sure you have the language files installed:

.. code:: bash

    sudo dnf install aspell-en hunspell-en


Then, to check all your :code:`.tex` files, you can use something like this:

.. code:: bash

    find . -name "*.tex" -exec aspell --lang=en --mode=tex check "{}" \; # Aspell
    find . -name "*.tex" -exec hunspell -t -i utf-8 '{}' \; # Hunspell

I looked around a bit, and decided to use Hunspell_. It's used by LibreOffice, Firefox, and other applications. I commit my work first and then run the above command which opens a window like this:

.. image:: {static}/images/hunspell-example.png
    :alt: Hunspell screenshot
    :target: {static}/images/hunspell-example.png
    :width: 750px

Once you've gone through it and made your changes, you can then use :code:`git diff --word-diff` to review your changes. If you'd like to undo some of them, use :code:`git add -i` and so on:

.. image:: {static}/images/git-word-diff.png
    :alt: Git diff screenshot
    :target: {static}/images/git-word-diff.png
    :width: 750px

That's it! Happy writing!

.. _Aspell: http://aspell.net/
.. _Hunspell: http://hunspell.github.io/
.. _LaTeX: https://latex-project.org/intro.html
