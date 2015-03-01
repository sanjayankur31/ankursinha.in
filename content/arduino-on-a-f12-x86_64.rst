Arduino on a F12 x86_64
#######################
:date: 2009-12-29 17:43
:author: ankur
:category: FOSS
:tags: arduino, Fedora 12
:tags: arduino, Fedora 12
:tags: arduino, Fedora 12
:tags: arduino, Fedora 12
:slug: arduino-on-a-f12-x86_64

I just started playing around with `arduino`_ boards.  There's a F11
how-to given `here`_. Some things to remember for a 64bit Fedora.

-  `Install Sun Java`_ , a F12 x86\_64 system needs the Linux64 package.
-  Set up your system to use Sun Java as given
   `here <http://fedorasolved.org/browser-solutions/java-i386/>`__.
   (Step 5 onwards)
-  Follow the howto link I've given above.
-  That's it :)

As a side note, it seemed to work with OpenJDK too, (reset the
alternatives to point to OpenJDK and tested)

.. _arduino: http://www.arduino.cc/
.. _here: http://www.arduino.cc/playground/Linux/Fedora
.. _Install Sun Java: http://java.sun.com/javase/downloads/index.jsp
