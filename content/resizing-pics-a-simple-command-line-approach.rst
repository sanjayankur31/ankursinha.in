Resizing pics : A simple command line approach
##############################################
:date: 2010-11-06 18:17
:author: ankur
:category: Tech
:slug: resizing-pics-a-simple-command-line-approach

First install the required package:

::

    $ yum install ImageMagick

Then,

::

    $ cd /path/to/photos/to/resize
    $ for i in *.JPG ; do convert $i -resize 25% new$i; done

That's pretty much it! This is very very simple. You might have to check
if the file names have spaces etc. (my camera gives me DSC?????.JPG, so
this works)

For more info on "convert"

::

    $ man convert 

