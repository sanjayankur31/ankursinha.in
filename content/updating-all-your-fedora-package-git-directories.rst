Updating all your fedora package git directories
################################################
:date: 2012-02-23 20:34
:author: ankur
:category: Tech
:tags: Fedora
:slug: updating-all-your-fedora-package-git-directories

Most package maintainers already know this (*or use something way
easier*), but this is how I go about updating all my fedora package git
folders:

::

    [ankur@ankur ~]$ cd Documents/work/repos/others/fedora-packages/
    [ankur@ankur fedora-packages]$ ls
    aeskulap  dcm4che-test       fpaste        hiran-perizia-fonts  libmpd       memaker                OpenNL                python-hl7  subversion    trash-cli
    cmake     detex              freemedforms  Inventor             libtorrent   mpdas                  OSGi-bundle-ant-task  rssdler     suitesparse   vtk
    comps     django-authopenid  gdcm          klt                  libtpcimgio  nifticlib              pyclutter             rtorrent    toothchart    xmedcon
    curlpp    evolution-rss      gnumed        libgexiv2            libtpcmisc   oldstandard-sfd-fonts  pystache              scout       transmission  zlib
    [ankur@ankur fedora-packages]$ for i in `ls`; do cd "$i"; git pull; cd ..; done
    remote: Counting objects: 5, done.
    remote: Compressing objects: 100% (3/3), done.
    Unpacking objects: 100% (3/3), done.
    remote: Total 3 (delta 2), reused 0 (delta 0)
    From ssh://pkgs.fedoraproject.org/aeskulap
     * [new branch]      f17        -> origin/f17
       ca0fa88..ef4f943  master     -> origin/master
    Updating ca0fa88..ef4f943
    Fast-forward
     aeskulap.spec |    5 ++++-
     1 files changed, 4 insertions(+), 1 deletions(-)
    remote: Counting objects: 20, done.
    remote: Compressing objects: 100% (17/17), done.
    ..

Moments later, all of them are up to date.
