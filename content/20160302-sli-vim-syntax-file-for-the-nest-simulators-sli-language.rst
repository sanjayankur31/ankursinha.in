sli.vim - syntax file for the NEST simulator's SLI language
###########################################################
:date: 2016-03-02 10:53:58
:author: ankur
:category: Research
:tags: Computational neuroscience, Fedora, Programming, Vim, NEST, sli-vim
:slug: sli-vim-syntax-file-for-the-nest-simulators-sli-language
:summary: I've hacked up a syntax file for `NEST <http://nest-simulator.org>`__'s `SLI <http://www.nest-simulator.org/quickref/>`__ simulation language. It is by no means complete, but it already makes reading and writing SLI a lot easier.

I've been reading some of `NEST <http://nest-simulator.org>`__'s `SLI <http://www.nest-simulator.org/quickref/>`__ examples to understand the simulation better. I noticed that these files had no syntax highlighting at all which made the code difficult to read. I couldn't find a syntax highlighting file for Vim anywhere so I've begun writing my own. It isn't complete, and I'm sure it's buggy, but it already seems to make reading and writing SLI easier. Here's what it makes an SLI file look like:

.. image:: {static}/images/20160302-sli-vim.png
    :width: 500px
    :alt: Screenshot showing SLI syntax highlighting in Vim
    :align: center
    :target: {static}/images/20160302-sli-vim.png

Installation
-------------

It's just a syntax file. You can drop it in ``~/.vim/syntax/`` directory (on Linux) or you can use `pathogen <https://github.com/tpope/vim-pathogen>`__ and just clone the repository and so on. Once done, add this to your ``vimrc`` file:

.. code:: vim

    au BufRead,BufNewFile *.sli set filetype=sli
    au FileType sli setl foldenable foldmethod=syntax 

The file is `hosted on Github <https://github.com/sanjayankur31/sli.vim>`__. Feel free to open issues, or even better, pull requests ;)
