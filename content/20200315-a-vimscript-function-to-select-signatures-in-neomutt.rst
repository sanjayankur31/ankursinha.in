A Vim script function to select signatures in Neomutt
#####################################################
:date: 2020-03-15 09:39:20
:author: ankur
:category: Tech
:tags: Planet, Vim, Neomutt, Fedora
:slug: a-vimscript-function-to-select-signatures-in-neomutt
:summary: I was dabbling in `Vim script`_ and wrote myself a simple function to
          select signatures when composing e-mails in Neomutt_.


I've been using Neomutt_ for a `while now
<{filename}/20171203-transitioning-to-neomutt-and-friends-for-e-mail.rst>`__.
It allows me to stick to the Byobu_ based terminal workflow that I'm used to.
Most importantly, it lets me use Vim_ to write my e-mails, so I don't need to
really learn another tool now.

Neomutt_ can be configured to add a signature at the end of the e-mail, and one
can select a signature depending on various parameters, such as the senders
address using `hooks <https://neomutt.org/man/neomuttrc>`__. However,
sometimes, one does need to select other signatures.

The simple Vim_ way, of course, is to simply delete the last few lines, and
then read in the new signature using :code:`:r <filename>`. This takes a few
more key strokes than one would like (well, than I like) so I thought I'd
dabble in `Vim script`_ a bit and automate it. Here's what I've come up with:


.. code:: vim

    " A function to load the right signature when I'm using neomutt
    function! LoadSignature(signature)
        " Only work for mail files
        let this_file_type = &filetype
        if this_file_type != "mail"
            echo "This is not a mail file! Not running!"
            return 1
        endif

        " Get the current signature's line
        " Go to last line
        let saved_cursor_position = getpos('.')
        " Set cursor to file end and search backwards
        call cursor(99999999999999999999, 0)
        let l:sigstart = search('-- ', 'b')
        " Confirm that the line was found
        if sigstart == 0
            echo "No signatures detected."
            return 1
        endif

        " Check if signature file exists
        let l:sigdir = escape(expand('$HOME'), '\') . "/Sync/99_private/neomuttdir/"
        let l:sigfile = sigdir . a:signature . ".sig"
        if filereadable(sigfile)
            " delete the current lines after the "-- " line
            let l:delstart = sigstart + 1
            execute delstart . ",$d"
            " Read the new signature
            execute sigstart . "read " . sigfile
            " Return cursor to wherever it was
            call setpos('.', saved_cursor_position)
        else
            echo "File " . sigfile . " not found!"
            echo "Available signature files:\n" . globpath(sigdir, '*.sig')
        endif
    endfunction

So, adding this to :code:`~/.vimrc` would let one run :code:`:call
LoadSignature('signature')` in Vim_ to select a signature. Each signature is a
different file with a :code:`.sig` file extension in the location given by
:code:`sigdir`, and the name of the file is the argument that needs to be given
to the function. If the signature file cannot be found, it'll list available ones.

It's quite simple really, and I'm sure it can be made better, but it works.


.. _Vim script: https://en.wikipedia.org/wiki/Vim_(text_editor)#Vim_script
.. _Neomutt: https://neomutt.org/
.. _Vim: https://www.vim.org/
.. _Byobu: https://www.byobu.org/
