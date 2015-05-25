making vim-latex load when you open a new tex file
##################################################
:date: 2010-11-23 20:43
:author: ankur
:category: Other
:tags: Fedora
:slug: making-vim-latex-load-when-you-open-a-new-tex-file

For quite sometime now, I've been pondering over this issue:
`vim-latex`_ wouldn't load when I began writing a new .tex file. As a
result, I'd get errors such as ":TTemplate command not found". I found
the "bug" today. From the `vim-latex site`_:

::

    " OPTIONAL: Starting with Vim 7, the filetype of empty .tex files defaults to
    " 'plaintex' instead of 'tex', which results in vim-latex not being loaded.
    " The following changes the default filetype back to 'tex':
    let g:tex_flavor='latex'

Make sure you add this to your .vimrc if you want vim-latex to work as
expected.

.. _vim-latex: http://vim-latex.sourceforge.net/index.php
.. _vim-latex site: http://vim-latex.sourceforge.net/documentation/latex-suite/recommended-settings.html
