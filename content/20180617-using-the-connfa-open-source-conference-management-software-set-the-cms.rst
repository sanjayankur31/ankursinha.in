Using the Connfa open source conference management software set: the CMS
########################################################################
:date: 2018-06-22 23:36:23
:author: ankur
:category: Tech
:tags: Community, Conference, Android, Fedora
:slug: using-the-connfa-open-source-conference-management-software-set-the-cms
:summary: The Connfa_ open source suite looks like a great set of tools
          for conference management. It consists of a web application, a
          central CMS integration server, and mobile applications for both
          Android and iOS. I was looking at how one could use the mobile
          applications. The mobile applications get their data from the
          integration server, which provides an API. So, I looked at how to set
          it up and document my findings in this post.

The Connfa_ open source suite looks like a great set of tools for conference
management. It consists of a web application, a central CMS integration server,
and mobile applications for both Android and iOS. I was looking at how one
could use the mobile applications. The mobile applications get their data from
the integration server, which provides an API. So, I looked at how to set it up
and document my findings in this post.


The Connfa_ CMS server is a php application that uses a MySQL database.  To
begin with, the documentation here is quite good:
http://connfa.com/documentation/.  However, as is usually seen, it takes a
few tweaks to deploy it.  These steps are therefore, Fedora 28 specific.

On Fedora, one needs to use php71 from remi's repository:
https://blog.remirepo.net/pages/Config-en

.. code:: bash

    sudo dnf install php71 composer php71-php-mysqlnd mariadb httpd mariadb-server php71-php-xml
    sudo systemctl start php71-php-fpm
    sudo systemctl start httpd
    sudo systemctl start mysqld
    module load php71
    php --version


This is because the tool doesn't work with the latest version of php that's in
Fedora 28. The tool also has a bug or two, so I used this fork that appears to
have a bugfix:

https://github.com/d-i-t-a/connfa-integration-server/tree/develop

Then, one must set up Mariadb_ as explained here:
https://fedoraproject.org/wiki/MariaDB. Note that Mariadb_ is an Open source
MySQL implementation.

One must also create a database as explained in the wiki page, and a user that
connfa can use, which must match the values in the :code:`env` file.

On Fedora, I enabled the :code:`UserDir` httpd extension, and placed the
connfa-integration-server in :code:`~/public_html/`, since I didn't want to
work as root in :code:`/var/www/html` all the time. :code:`httpd` will needs to
be started and enabled:

.. code:: bash

    sudo systemctl start httpd; sudo systemctl enable httpd

On Fedora, Selinux must be asked to allow access to UserDirs:

.. code:: bash

    sudo setsebool -P httpd_read_user_content 1
    sudo setsebool -P httpd_unified 1
    sudo setsebool -P httpd_can_network_connect_db 1
    sudo setsebool -P httpd_can_network_connect 1


One can follow the steps from here next:
http://connfa.com/integration-server/server-requirements

I also run :code:`composer update` to update the php bits.

Then, update the env file and so on as explained here:
http://connfa.com/integration-server/install/


.. code:: bash

    php artisan key:generate #sets the keys in the env file
    php artisan password:change --name=admin --password=connfa18

The site should be accessible at http://localhost/~<username>/public/login/
The username is :code:`admin@test.com` here.

The API is accessible at:
http://localhost/~<username>/public/api/v2/cns-2018/checkUpdates

I did have quite a few issues with permissions, but then I'm neither a web
developer nor a server administrator, so my skills in the department are rather
limited.

I'll look at the Android application next, and hopefully, I'll be able to sync
it up with the CMS server.

.. _Connfa: http://connfa.com/
.. _Mariadb: https://mariadb.org/
