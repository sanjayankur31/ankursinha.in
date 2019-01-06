pdfpc - now in the Fedora repositories
######################################
:date: 2015-06-24 21:01:33
:author: ankur
:category: Tech
:tags: Fedora, Linux
:slug: pdfpc-now-in-the-fedora-repositories
:summary: pdfpc is now available in the Fedora repositories and can be installed using DNF.

I'd `written about pdfpc earlier <{filename}/20150615-pdfpc.rst>`_. I packaged it for Fedora and you can now install it directly using DNF. It's still in the testing repositories, so you'll need to enable the repository for the time being. I'm leaving the copr repository as it is, but please note that I will not update the packages there any more.

.. code-block:: bash

    $ sudo dnf install pdfpc --enablerepo=updates-testing

If you do test the package, please give karma to `the update on Bodhi`_. If you'd like to help the Fedora QA team with testing in general, please look at `the wiki page`_.

Cheers!

.. _the update on Bodhi: https://admin.fedoraproject.org/updates/FEDORA-2015-10586/pdfpc-4.0.0-2.fc22
.. _the wiki page: https://fedoraproject.org/wiki/QA:Updates_Testing
