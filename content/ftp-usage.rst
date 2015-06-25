FTP usage
#########
:date: 2011-10-04 01:34
:author: ankur
:category: Tech
:tags: Fedora
:slug: ftp-usage

|image0| |image1| |image2|

 

 

At the end of my `last post`_, I had mentioned that a combination of
swiFTP and ftp is  a convenient way of syncing your notes. Now, I make
it even easier! Write a script like so:

::

    cd ~/.local/share/gnote/

    ftp -n $1 2121 << EndOfCommand123
    user myswiftpusername myswiftppassword
    cd sdcard/tomdroid
    put file1.note
    put file2.note
    put file3.note
    put file4.note
    put file5.note
    close
    EndOfCommand123

    exit 0

**The explanation:**

To run it, provide it with executable permissions (using chmod), and
execute it after switching on the swiFTP server on your phone:
./myscript.sh [ip of phone as reported by swiFTP]

One needs to first locate what files need to be synced. I grepped my
note files to find out the ones that I need synced every night. You can
also open them in a text editor. The .note files are really just xml
files. For more ftp commands, please look at its manual.

.. _last post: http://dodoincfedora.wordpress.com/2011/09/30/using-your-gnotes-on-your-android-phone/

.. |image0| image:: http://dodoincfedora.files.wordpress.com/2011/09/gnote.png
   :target: http://dodoincfedora.files.wordpress.com/2011/09/gnote.png
.. |image1| image:: http://dodoincfedora.files.wordpress.com/2011/09/swiftp.jpg
   :target: http://dodoincfedora.files.wordpress.com/2011/09/swiftp.jpg
.. |image2| image:: http://dodoincfedora.files.wordpress.com/2011/09/tomdroid.jpg
   :target: http://dodoincfedora.files.wordpress.com/2011/09/tomdroid.jpg
