Fedora free-media-tool version 0.2alpha
#######################################
:date: 2012-02-16 01:01
:author: ankur
:category: Tech
:tags: Fedora
:slug: fedora-free-media-tool-version-0-2alpha

I've managed to get most of the functionality coded up. Here's what
ffmtool -h looks like now (on my system):

.. code-block:: bash

    [ankur@ankur ~]$ ffmtool -h
    [+] Parsing available options from config file: /home/ankur/.config/fedora-free-media-tool/config.cfg
    Usage: ffmt [Options] [args]...
    A tool to assist Fedora free-media contributors.
    Without options, it prints pending envelopes to the current directory using default values of input and database files.

    Options:
      -h [ --help ]                         Print this usage message.
      -c [ --config-file ] [=arg(=/home/ankur/.config/fedora-free-media-tool/config.cfg)]
                                            Configuration file

      -d [ --database ] [=arg(=/home/ankur/.local/share/fedora-free-media-tool/free-media-database.db)]
                                            Complete output file path

      -x [ --fas-username ] arg             FAS Username. Password will be asked if
                                            required.
                                            No command line option is provided to
                                            enter password to avoid entering of
                                            password in plaintext on the terminal.
                                            Use with -u

      -i [ --import ] [=arg(=/home/ankur/.local/share/fedora-free-media-tool/report.csv)]
                                            Import data
                                            Optional argument: Complete input file
                                            path

      -r [ --resolve ] arg                  Change status of provided ticket
                                            numbers to RESOLVED
                                            (default: 0 meaning all new tickets)

      -e [ --reset ] arg                    Change status of provided ticket
                                            numbers to PENDING
                                            (default: 0 meaning all fixed tickets)

      -A [ --assign-to-lc ] arg             Assign these tickets to a Local Contact
                                            (default: 0 meaning all)

      -f [ --force ] arg                    Force import even if the ticket exists
                                            in database

      -a [ --add-new ] arg                  Manually add a new entry: unimplemented

      -m [ --modify ] arg                   Modify the address in a ticket entry.
                                            Generally required when the address is
                                            malformed and the splitter can't handle
                                            it.
                                            arg: Ticket number

      -o [ --output-dir ] [=arg(=./)]       Directory to put the printed envelopes

      -P [ --print-ticket-info ] arg        Print ticket info for any one ticket
                                            number

      -p [ --print ] arg                    List of ticket numbers to print
                                            envelopes for
                                            (default: 0 meaning all new tickets)

      -l [ --list ] [=arg(=all)]            List records in database
                                            all,pending,complete,local-contact

      -L [ --list-long ] [=arg(=all)]       List records with description
                                            all,pending,complete,local-contact

      -u [ --update ] arg                   Download latest report from the trac
                                            and update the database
                                            This automatically stores the
                                            information in default database
                                            directory

      -v [ --v-level ] [=arg(=0)]           Debug level: 1,2,3

      -n [ --sender-name ] arg              Senders name

      -s [ --sender-add ] arg               Senders address
                                            Use % as a line limiter

      -t [ --template ] [=arg(=/usr/share/fedora-free-media-tool/free-media-mailer.png)]
                                            Location of envelope template

      -V [ --version ] arg                  Package information: version etc.

    [ankur@ankur ~]$

Not bad eh? It's probably going to have quite a few bugs yet. I haven't
managed to test it out thouroughly yet. You can help ;)

Installation:
-------------

If you're on an x86\_64, you're in luck! `Use this rpm`_.

I haven't been able to build an rpm for i386 systems yet because of
`this bug in curlpp.`_

On a fedora system, you'll need the following packages:

::

     yum install sqlite-devel ImageMagick-c++-devel curlpp-devel boost-devel

Download the `source here`_

Untar it anywhere, and then, the usual autotool steps

::

    ./configure --datadir=/usr/share
    #datadir needs to be defined
    #this is where the envelope template is kept

    make
    make install # as root

That's all!

Example usage:
--------------

::

    [ankur@ankur SPECS]$ ffmtool -u
    [+] Parsing available options from config file: /home/ankur/.config/fedora-free-media-tool/config.cfg
    [+] /home/ankur/.config/fedora-free-media-tool/ already exists. Continuing..
    [+] /home/ankur/.local/share/fedora-free-media-tool/ already exists. Continuing..
    Username: ankursinha
    Password:
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
      0     0    0     0    0     0      0      0 --:--:--  0:00:03 --:--:--     0
    100  5815  100  5815    0     0   3152      0  0:00:01  0:00:01 --:--:--  6889
    [+] Datafile set to: /home/ankur/.local/share/fedora-free-media-tool/report.csv
    [+] Databasefile set to: /home/ankur/.local/share/fedora-free-media-tool/free-media-database.db
    [+] Database already exists. Continuing..
    [X] File format should be:
    1.1st line is a header
    2.One record per line (including address)
    3.Please ensure description consists only of address (personal message from requestor if any should be removed)
    4.Each new address line begins with a ",[[BR]]"
    [X] Example:
    [X] Number of lines in file without header is 27 while number of records found is 19
    [X] The difference suggests that some records are malformed. Please correct the records and use the -i option to import to database

Here, the file we downloaded was "malformed", because the ticket
submitter didn't punctuate his address properly (or added a comment).
Once you've gotten rid of the extra stuff from the data file:

::

    [ankur@ankur fedora-free-media-tool]$ ffmtool -i
    [+] Parsing available options from config file: /home/ankur/.config/fedora-free-media-tool/config.cfg
    [+] /home/ankur/.config/fedora-free-media-tool/ already exists. Continuing..
    [+] /home/ankur/.local/share/fedora-free-media-tool/ already exists. Continuing..
    [+] Datafile set to: /home/ankur/.local/share/fedora-free-media-tool/report.csv
    [+] Databasefile set to: /home/ankur/.local/share/fedora-free-media-tool/free-media-database.db
    [+] Database already exists. Continuing..
    [+] File seems well formatted. Proceeding to import.
    Entered worker import function..
    [+] Ticket 7353 already exists in table, skipping.
    [+] Ticket 7710 already exists in table, skipping.
    [+] Ticket 7816 already exists in table, skipping.
    [+] Ticket 7823 already exists in table, skipping.
    [+] Ticket 7835 already exists in table, skipping.
    [+] Ticket 7842 already exists in table, skipping.
    [+] Ticket 7855 already exists in table, skipping.
    [+] Ticket 7863 already exists in table, skipping.
    [+] Ticket 7896 already exists in table, skipping.
    [+] Ticket 7907 already exists in table, skipping.
    [+] Ticket 7916 already exists in table, skipping.
    [+] Ticket 7938 already exists in table, skipping.
    [+] Ticket 7945 already exists in table, skipping.
    [+] Ticket 7948 already exists in table, skipping.
    [+] Ticket 7949 imported to the database.
    [+] 15 records successfully imported into database.
    [ankur@ankur fedora-free-media-tool]$

You can use the various options to look/modify ticket entries in the
database. All this stuff will be on your local copy only. I don't see a
reason to update the trac info yet. The best part is, you can print your
fedora free-media envelopes using this tool:

.. code-block:: bash

    [ankur@ankur fedora-free-media-tool]$ ffmtool -l
    [+] Parsing available options from config file: /home/ankur/.config/fedora-free-media-tool/config.cfg
    [+] /home/ankur/.config/fedora-free-media-tool/ already exists. Continuing..
    [+] /home/ankur/.local/share/fedora-free-media-tool/ already exists. Continuing..
    All tickets in data base (ticket numbers only): 19
    #7353
    #7710
    #7816
    #7823
    #7835
    #7842
    #7855
    #7863
    #7884
    #7895
    #7896
    #7907
    #7916
    #7921
    #7922
    #7938
    #7945
    #7948
    #7949
    [ankur@ankur fedora-free-media-tool]$ ffmtool -p 7949 7948 7945
    [+] Parsing available options from config file: /home/ankur/.config/fedora-free-media-tool/config.cfg
    [+] /home/ankur/.config/fedora-free-media-tool/ already exists. Continuing..
    [+] /home/ankur/.local/share/fedora-free-media-tool/ already exists. Continuing..
    [+] Printed envelope for ticket number 7949 to ./free-mediaEnvelope7949.png.
    [+] Printed envelope for ticket number 7948 to ./free-mediaEnvelope7948.png.
    [+] Printed envelope for ticket number 7945 to ./free-mediaEnvelope7945.png.
    [+] Datafile set to: /home/ankur/.local/share/fedora-free-media-tool/report.csv
    [+] Databasefile set to: /home/ankur/.local/share/fedora-free-media-tool/free-media-database.db
    [+] Database already exists. Continuing..
    Marked ticket #7949
    Marked ticket #7948
    Marked ticket #7945
    [ankur@ankur fedora-free-media-tool]$ ls *.png
    free-mediaEnvelope7945.png  free-mediaEnvelope7948.png  free-mediaEnvelope7949.png
    [ankur@ankur fedora-free-media-tool]$

| This is what the envelope would look like:
|  |example generated envelope|

You can print all the envelopes at one go, or print them one at a time.

Since I'm using boost::program\_options to take arguments, all the
arguments can be specified in the config file. I've also `put up an
example config file`_ that you can refer.

As always, feed back is welcome. You're welcome to review my code and
point out improvements! This was supposed to be a practice project after
all. You're most welcome to submit patches too! The `git repository is
hosted on gitorious.`_

Phew! Long post, probably the longest I've ever written. Cheers!

.. _Use this rpm: http://ankursinha.fedorapeople.org/fedora-free-media-tool/fedora-free-media-tool-0.2-1.fc16.x86_64.rpm
.. _this bug in curlpp.: https://bugzilla.redhat.com/show_bug.cgi?id=788639
.. _source here: http://ankursinha.fedorapeople.org/fedora-free-media-tool/fedora-free-media-tool-0.2alpha.tar.gz
.. _put up an example config file: http://ankursinha.fedorapeople.org/fedora-free-media-tool/config.cfg
.. _git repository is hosted on gitorious.: https://gitorious.org/fedora-free-media-tool

.. |example generated envelope| image:: http://ankursinha.in/wp/wp-content/uploads/2012/02/free-mediaenvelope7949.png?w=212
   :target: http://ankursinha.in/wp/wp-content/uploads/2012/02/free-mediaenvelope7949.png
