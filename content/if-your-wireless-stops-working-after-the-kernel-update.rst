If your wireless stops working after the kernel update
######################################################
:date: 2011-08-13 17:55
:author: ankur
:category: Tech
:tags: Fedora
:slug: if-your-wireless-stops-working-after-the-kernel-update

... as root, run this in a terminal: echo "blacklist bcma" >>
/etc/modprobe.d/broadcom-wl-blacklist.conf
