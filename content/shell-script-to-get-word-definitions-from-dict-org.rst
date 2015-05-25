shell script to get word definitions from dict.org
##################################################
:date: 2010-12-01 00:18
:author: ankur
:category: Tech
:tags: Bash
:slug: shell-script-to-get-word-definitions-from-dict-org

Edit : There's a list of\ `command line clients for dict.org here`_
already, came across if **after** I had written the script. What a pity
:/

So, 

::

    $ su -c  'yum -y install dictd'
    $ dict -f fedora
    3 definitions found
    dict.org        2628    gcide   The Collaborative International Dictionary of English v.0.48
      fedora fe*do"ra (f[i^]*d[^o]r"[.a]), n.
         A soft felt hat with a crown creased lengthwise.

         Syn: felt hat, homburg, Stetson, trilby.
              [WordNet 1.5]
    dict.org        2628    wn      WordNet (r) 2.0
      fedora
           n : felt hat with a creased crown [syn: {felt hat}, {homburg}, {Stetson},
                {trilby}]
    dict.org        2628    gazetteer       U.S. Gazetteer (1990)
      Fedora, SD
        Zip code(s): 57337

| Cheers!
|  ---------

Developers are lazy. Recently, I had published a post on `command line
text utils`_. One of the utils was to use **curl**\ to access the
`dict.org`_ database. I got bored of using the command again and again,
so I chucked it into a shell script. It's highly rudimentary, and
doesn't validate or check for errors etc. yet, but works.

::

    #!/bin/bash

    # Copyright 2010 Ankur Sinha
    # Author: Ankur Sinha
    #
    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.
    #
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.
    #
    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <http://www.gnu.org/licenses/>
    #
    # File : dict_org : A simple shell script to get definitions from dict.org
    #
    # TODOS :   - add error handling for output
    #                 - structure output

    main()
    {

        # check if curl is installed
        if [ ! -f /usr/bin/curl ] ; then
            echo -e "This script requires curl to function.nPlease use your
    package manager and install curl.nOn a Fedora system, run:
    $ su -c 'yum install curl'"
            exit 2
        fi

        # get definition
        definition=$( curl -s dict://dict.org/d:"$1")

        echo "$definition" | more

        exit 0
    }

    # check for correct usage
    if [ $# -ne 1 ] ; then
        echo -e "Usage : $0  nThis shell script takes only one argument,
    the word you want to look up at dict.org"
        exit 1
    fi

    main $1

I've also uploaded it `here`_

.. _command line clients for dict.org here: http://www.dict.org/links.html
.. _command line text utils: http://dodoincfedora.wordpress.com/2010/11/22/note-to-self-command-line-text-utils/
.. _dict.org: http://dict.org
.. _here: http://ankursinha.fedorapeople.org/dict_org.sh
