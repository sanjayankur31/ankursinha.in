Using the Connfa open source conference management software set: the CMS
########################################################################
:date: 2018-06-17 20:29:59
:author: ankur
:category: Tech
:tags: Community, Conference, Android
:slug: using-the-connfa-open-source-conference-management-software-set-the-cms
:status: draft
:summary: The Connfa_ set of open source suite looks like a great set of tools
          for conference management. It consists of a web application, a
          central CMS integration server, and mobile applications for both
          Android and iOS. I was looking at how one could use the mobile
          applications. The mobile applications get their data from the
          integration server, which provides an API. So, I looked at how to set
          it up and document my findings in this post.

The documentation here is quite good: http://connfa.com/documentation/

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

Then, one must set up Mariadb as explained here:
https://fedoraproject.org/wiki/MariaDB

One must also create a database, and a user that connfa can use, which must
match the values in the :code:`env` file.

On Fedora, I enabled the :code:`UserDir` httpd extension, and placed the
connfa-integration-server in :code:`~/public_html/`

:code:`httpd` will needs to be started and enabled:

.. code:: bash

    sudo systemctl start httpd; sudo systemctl enable httpd

On Fedora, Selinux must be asked to allow access to UserDirs:

.. code:: bash

    sudo setsebool -P httpd_read_user_content 1
    sudo setsebool -P httpd_unified 1
    sudo setsebool -P httpd_can_network_connect_db 1
    sudo setsebool -P httpd_can_network_connect 1


Then continue to follow the steps from
http://connfa.com/integration-server/server-requirements

I also run :code:`composer update`.

Then, update the env file and so on as explained here:
http://connfa.com/integration-server/install/


.. code:: bash

    php artisan key:generate
    php artisan password:change --name=admin --password=connfa18

Username: admin@test.com, password whatever is set.


The API is accessible at:
http://localhost/~asinha/public/api/v2/cns-2018/checkUpdates

.. _Connfa: http://connfa.com/
