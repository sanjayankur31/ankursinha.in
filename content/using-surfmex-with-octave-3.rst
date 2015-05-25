Using SURFmex with Octave
#########################
:date: 2012-08-22 07:47
:author: ankur
:category: Tech
:tags: Fedora
:slug: using-surfmex-with-octave-3

This isn't so much as for others as it's a "note to self".

.. raw:: html

   <div>

I've recently begun actual work at my research course. Obviously, I
prefer to use `Octave`_ to Matlab. Here's how to use the \ `SURFmex
toolkit for Matlab`_ with Octave:

.. raw:: html

   </div>

.. raw:: html

   <div>

`Download the source`_ and unzip it someplace. You can get rid of the
mexw{32,64} directories, since they're binaries for Windoz.

.. raw:: html

   </div>

.. raw:: html

   <div>

Create a folder called mex, just to keep all our output mex files
together.

.. raw:: html

   </div>

.. raw:: html

   <div>

Install the opencv-devel package. On fedora:

.. raw:: html

   </div>

.. raw:: html

   <div>

::

    $ su -c 'yum install opencv-devel'

.. raw:: html

   </div>

.. raw:: html

   <div>

Then, compile the cpp files into mex files:

.. raw:: html

   </div>

.. raw:: html

   <div>

::

    $ mkoctfile-3.6.2 --mex -v `pkg-config --libs --cflags opencv` surfpoints.cpp

.. raw:: html

   </div>

.. raw:: html

   <div>

::

    $ mkoctfile-3.6.2 --mex -v `pkg-config --libs --cflags opencv` surfmatch.cpp

.. raw:: html

   </div>

.. raw:: html

   <div>

::

    # Move them to your mex folder:

.. raw:: html

   </div>

.. raw:: html

   <div>

::

    $ mv *.mex mex/ -v

.. raw:: html

   </div>

.. raw:: html

   <div>

You should now have two mex files generated:

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   <div>

::

    [ankur@ankur SURFmex-v2(master *%)]$ cd mex/
    [ankur@ankur mex(master *%)]$ ll
    total 484
    rwxrwxr-x. 1 ankur ankur 219400 Aug 22 11:20 surfmatch.mex
    rwxrwxr-x. 1 ankur ankur 273339 Aug 22 11:20 surfpoints.mex

.. raw:: html

   </div>

.. raw:: html

   <div>

That's pretty much it. All the hints were in the make.m file really.

.. raw:: html

   </div>

.. raw:: html

   <div>

To run one of the examples:

.. raw:: html

   </div>

.. raw:: html

   <div>

Copy an image to the examples folder and name it peppers.png. This
appears to be one of the default images that matlab provides.

.. raw:: html

   </div>

.. raw:: html

   <div>

::

    $ cd examples/
    octave
    octave>
    octave> addpath ../mex  % add the mex files to path
    octave> addpath ../common  % add the common functions to the path
    octave> path % check your path
    octave> small_example

.. raw:: html

   </div>

.. raw:: html

   <div>

Your screenshot won't look like this. I've modified the example a little
to use different images.

.. raw:: html

   </div>

.. raw:: html

   <div>

|SURFmex example image|

.. raw:: html

   </div>

.. raw:: html

   </div>

.. _Octave: http://www.gnu.org/software/octave/
.. _SURFmex toolkit for Matlab: http://www.maths.lth.se/matematiklth/personal/petter/surfmex.php
.. _Download the source: http://dstats.net/fwd/tbaok

.. |SURFmex example image| image:: http://ankursinha.in/wp/wp-content/uploads/2012/08/surfimage.png?w=300
   :target: http://ankursinha.in/wp/wp-content/uploads/2012/08/surfimage.png
