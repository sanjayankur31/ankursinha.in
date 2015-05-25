LaTeX, vim and Fedora
#####################
:date: 2012-03-13 00:55
:author: ankur
:category: Tech
:tags: Fedora
:slug: latex-vim-and-fedora

I'm a vim junkie (In spite of Sindre's numerous events to convert me
into an Emacs person!). I'm also a LaTeX junkie. There are quite a few
reasons behind my love for LaTeX:

.. raw:: html

   <div>

-  Easy to use (Yes! Once you get the hang of it, it's *very* easy!)
-  Takes care of the dirty work: You need to work on the subject matter,
   it takes care of the formatting for you!
-  Free software license: \ http://www.latex-project.org/lppl/
-  ..

.. raw:: html

   <div>

There are numerous other reasons, such as easy bibliography management,
for instance. You'll learn these advantages once you begin using LaTeX
regularly. This post is not intended to convert anyone into a LaTeX
user, rather, it's for folks who'd like to use LaTeX and vim on their
Fedora systems. This post is Fedora specific. However, most of the tips
should be valid on any operating system using LaTeX and vim.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

System setup
------------

.. raw:: html

   <div>

1. Install required packages

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Set up Jindrich's texlive repository. (Thanks Jindrich!). The
instructions for Fedora 15 and 16 can be found at this wiki
page: \ http://fedoraproject.org/wiki/Features/TeXLive

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

::

    su -c 'yum install vim-enhanced vim-latex vim-X11 texlive texlive-bibtex-bin texlive-latex-bin-bin'

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

As the wiki mentions, you can install other required texlive components
also. I'm working with a minimal setup here.

.. raw:: html

   </div>

Vimrc setup
-----------

.. raw:: html

   <div>

We need to make some additions to our **~/\ *.vimrc*** file. The
following lines work for me:

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   <div>

" Enable filetype plugins

.. raw:: html

   </div>

.. raw:: html

   <div>

filetype on

.. raw:: html

   </div>

.. raw:: html

   <div>

filetype plugin indent on

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

" latex stuff

.. raw:: html

   </div>

.. raw:: html

   <div>

let g:tex\_flavor='latex'

.. raw:: html

   </div>

.. raw:: html

   <div>

" indentation for tex files

.. raw:: html

   </div>

.. raw:: html

   <div>

au FileType tex set sw=2

.. raw:: html

   </div>

.. raw:: html

   <div>

"Spell check

.. raw:: html

   </div>

.. raw:: html

   <div>

au FileType tex setlocal spell spelllang=en\_gb

.. raw:: html

   </div>

.. raw:: html

   <div>

" Vim-latex rules:

.. raw:: html

   </div>

.. raw:: html

   <div>

" to enable ll to run automatically for pdfs

.. raw:: html

   </div>

.. raw:: html

   <div>

let g:Tex\_DefaultTargetFormat='pdf'

.. raw:: html

   </div>

.. raw:: html

   <div>

let g:Tex\_MultipleCompileFormats='dvi,pdf'

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

The comments tell you why these are needed, in brief. For complete
explanations, you can... **google up**!

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Getting down to writing LaTeX code and generating pdf files
-----------------------------------------------------------

.. raw:: html

   </div>

.. raw:: html

   <div>

Now that we have our system set up, lets write some LaTeX and use the
tools we've installed.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

`Here's the presentation`_ I had made for FUDCon Pune last year. You can
pick up code snippets from there.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Some tips (limited to VIM on the terminal):

.. raw:: html

   </div>

.. raw:: html

   <div>

-  Command "**:TTemplate**\ " -> pick from  4 ready templates provided
   by vim-latex
-  **ll** -> In command mode, compile your file. vim-latex will run
   pdflatex multiple times along with bibtex as required.
-  **lv** -> In command mode, view the generated pdf file
-  **: !bibtex %:r**\ run bibtex to make your bibliography. (%:r is the
   filename without the extension). This is not required with vim-latex
-  **]s** -> next bad spelling
-  **[s** -> previous bad spelling
-  **z=** -> pop up list of spelling suggestions
-  **SSE** -> macro for new section
-  **SSS** -> macro for new subsection
-  **SS2** -> macro for new subsubsection
-  Similar BibTeX shortcuts available for editing your bibliography.

.. raw:: html

   <div>

These are just some of the many, many commands that make working on
LaTex in VIM a breeze. For bibliography management, I currently use
**bibus**. There are quite a few bibliography managers available in the
fedora repositories. Try them out, use one that suits you.

.. raw:: html

   </div>

.. raw:: html

   </div>

More detailed documentation
---------------------------

.. raw:: html

   <div>

A list of more detailed documentation:

.. raw:: html

   </div>

.. raw:: html

   <div>

-  LaTeX wiki book: \ http://en.wikibooks.org/wiki/LaTeX/
-  My presentations on `LaTeX and Beamer(presentations using LaTeX)`_
   for dummies.
-  vim-latex documentation
   page: \ http://vim-latex.sourceforge.net/documentation/latex-suite.html
-  vim spelling help: \ http://vimdoc.sourceforge.net/htmldoc/spell.html
-  The interweb has more, just go look!

.. raw:: html

   <div>

I hope this makes LaTex writing easier for some of you!

.. raw:: html

   </div>

.. raw:: html

   </div>

.. _Here's the presentation: http://ankursinha.fedorapeople.org/LaTeX/LaTex.pdf
.. _LaTeX and Beamer(presentations using LaTeX): http://ankursinha.fedorapeople.org/LaTeX/
