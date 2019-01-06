Writing LaTeX well in Vim
#########################
:date: 2017-09-19 00:40:41
:author: ankur
:category: Tech
:tags: Calliope, Fedora, Free software, LaTeX, Vim
:slug: writing-latex-well-in-vim
:summary: Vim_ is a great text editor and LaTeX_ is a great document writing system. Since I write a lot of LaTeX_ for my research, I've been adding various Vim_ plug-ins to make my writing easier over the years. This post documents some of these additions.

Vim_ is a great text editor if one takes a bit of time to learn how to use it properly. There's quite enough documentation on how to use Vim_ correctly, and efficiently so I shan't cover that here. :code:`vimtutor` is an excellent resource to begin at.

Similarly, LaTeX_ is a `brilliant documentation system <https://www.google.co.uk/search?hl=en-GB&q=why+use+latex+for+writing>`__, especially for scientific writing if one takes the time to learn it. Unlike the usual Microsoft Word type systems, LaTeX_ is a set of commands/macros. Once the document is written using these, it must be compiled to produce a PDF document. It may appear daunting at first, but after one is familiar with it, it makes writing a breeze. Now, there are a editors especially designed for LaTeX_, but given that I use Vim_ for about all my writing, I use it for LaTeX_ too.

On Fedora, you can install Vim_ using DNF_: :code:`sudo dnf install vim-enhanced vim-X11`. I install the X11 package too to `use the system clipboard <http://vim.wikia.com/wiki/Accessing_the_system_clipboard>`__.

LaTeX tools
------------

To begin with, there are a few command line commands that one can use other than the necessary :code:`latex`, :code:`pdflatex`, :code:`bibtex`, :code:`biber`, and so on commands:

- :code:`latexmk` is a great tool that figures out the compilation sequence required to generate the document, and it does it for you.
- :code:`lacheck` and :code:`chktex` are both linters for LaTeX_ that make writing a lot easier.
- :code:`detex` strips a tex document of LaTeX_ commands to produce only the text bits.
- :code:`diction`, and :code:`style` give the `author an idea of the readability of the text <https://www.linux.com/news/improve-your-writing-gnu-style-checkers>`__.

One can use any text editor and then these utilities to improve their LaTeX_ writing experience.


On Fedora, install these with DNF_: :code:`sudo dnf install latexmk /usr/bin/lacheck /usr/bin/chktex /usr/bin/detex diction`. (Yes, you can tell DNF_ what file you want to install too!)

Built-in Vim features
----------------------

Vim_ already contains quite a few features that make writing quite easy;

- `Omni completion <http://vim.wikia.com/wiki/Omni_completion>`__ provides good suggestions based on the text under the cursor.
- There's in-built `spell checking <http://vimdoc.sourceforge.net/htmldoc/spell.html>`__ already.
- `Folding <http://vimdoc.sourceforge.net/htmldoc/fold.html>`__ logical bits makes the document easier to read and navigate through.
- `Syntax highlighting <http://vimdoc.sourceforge.net/htmldoc/syntax.html>`__ makes it a lot easier to read code by marking different commands in different colours.
- There are different flavours of `linenumbers <https://jeffkreeftmeijer.com/vim-number/>`__ that make moving about a document much simpler.
- At some point, the `conceal <http://vimdoc.sourceforge.net/htmldoc/syntax.html#conceal>`__ feature was added that further improves readability of documents
- `Buffers, tabs, windows <http://vimdoc.sourceforge.net/htmldoc/windows.html#windows>`__ are available in Vim_ too, of course.


Vim plug-ins
-------------

There are a lot of Vim_ plug-ins that extend some functionality or the other. The simplest way to install plug-ins is to use `Vundle <https://github.com/VundleVim/Vundle.vim>`__. Here are some plug-ins that I use. They're not all specific to LaTeX_.

- `Fastfold <https://github.com/Konfekt/FastFold>`__ makes folding faster.
- `vim-polyglot <https://github.com/sheerun/vim-polyglot>`__ provides better syntax highlighting for a many languages.
- `vim-airline <https://github.com/vim-airline/vim-airline>`__ provides an excellent, informative status line.
- `tagbar <https://github.com/majutsushi/tagbar>`__ lists sections (tags in general) in a different pane.
- `vim-colors-solarized <https://github.com/altercation/vim-colors-solarized>`__ provides the solarized themes for Vim_.
- `vimtex <https://github.com/lervag/vimtex>`__ provides commands to quickly compile LaTeX_ files, complete references, citations, navigate quicker, view the generated files, and so on.
- `ultisnips <https://github.com/SirVer/ultisnips>`__ provides lots of snippets for many languages, including LaTeX_. Get the snippets from the `vim-snippets <https://github.com/honza/vim-snippets>`__ plug-in.
- `YouCompleteMe <https://github.com/Valloric/YouCompleteMe>`__ is a completion engine that supports many languages. Remember that this one needs to be compiled!
- `Syntastic <https://github.com/vim-syntastic/syntastic/>`__ provides syntax checkers for many languages, including LaTeX_.

I've also used `vim-latex <https://github.com/vim-latex/vim-latex>`__ in the past and it's very very good. However, since I have other plug-ins that provide the various functionality that it brings together for many other languages too, I'm no longer using it. Worth a go, though.


An example document
--------------------

The image below shows a LaTeX_ file open in Vim_ with different plug-ins in action:

.. raw:: html

    <center>

.. image:: {static}/images/20170919-latex-vim.png
    :align: center
    :height: 800px
    :scale: 60 %
    :target: {static}/images/20170919-latex-vim.png
    :alt: Screenshot of Vim with a LaTeX file open showing various features.

.. raw:: html

    </center>

- On top, one can see the open buffer. Only one buffer is open at the moment.
- In the left hand side margin, one can see the fold indicators.
- The :code:`S>` bit is an indicator from the linter that Syntastic uses, showing a warning or an error.
- The line numbers are also visible in the left margin. Since I am in insert mode, they're just plain line numbers. Once one leaves insert mode, they change to relative.
- On line 171, the conceal feature shows Greek symbols instead of their LaTeX_ commands.
- Syntax highlighting is clearly visible. The commands have different colours. This is the solarized dark theme, of course.
- The "pop-up" shows Ultisnips at work. Here, I'm looking at adding a new equation environment.
- Underneath the pop up, the dashed line is a folded section. The :code:`+` symbol in the left margin implies that it is folded.
- In the status line, one can see that spell check is enabled, and that I'm using the :code:`en_gb` language.
- Next, the git status, and the git branch I'm in. That's the `vim-fugitive <https://github.com/tpope/vim-fugitive>`__ plug-in at work.
- Then, the filetype, the encoding, the number of words and so on provided by the airline plug-in.


Neat, huh? There is a lot more there that isn't easy to show in a screen-shot. For example, :code:`\ll` will compile the LaTeX_ file; :code:`\lv` opens the generated PDF file in a PDF viewer, Evince in my case; :code:`\lc` will clean the directory of any temporary files that were generated while compiling the document.

I keep all my `vimfiles on Github <https://github.com/sanjayankur31/vimfiles>`__. Feel free to take a look and derive your own. I tweak my configuration each time I find something new, though, so it may change rather frequently. Remember to read the documentation for whatever plug-ins in use. They provide a lot of options, lots of shortcuts, lots of other commands, and sometimes setting them up incorrectly can cause vim to behave in unexpected ways.

TL;DR: Use Vim_, and use LaTeX_!!

.. _Vim: https://vim.sourceforge.io/
.. _LaTeX: https://www.latex-project.org/
.. _DNF: https://github.com/rpm-software-management/dnf
