Updating your BIOS when you're not running Windows
##################################################
:date: 2012-11-06 13:42
:author: ankur
:category: Tech
:tags: Linux
:slug: updating-your-bios-when-youre-not-running-windows

Earlier today, I attempted to update my BIOS to the `latest version that
Dell provides me`_ with. My system doesn't suspend correctly, and this
was an attempt at covering all my bases `that Adam suggested in this bug
report`_. Alas, it didn't work - my system still doesn't suspend
correctly. Nevertheless, it did take me on a wild goose chase to figure
out how to actually update the BIOS since I lack a Windows installation
on my system.

What appeared to be the easiest way was using `System Rescue CD`_. This
didn't work for me somehow. I don't have any blank CDs around, and it
wouldn't boot from the USB that I created. I looked around to `try and
use it directly with Grub2`_, but it booted up a linux distribution
while I need `FreeDOS`_. I tussled a little with it and then gave up. I
decided to use a FreeDOS live cd. Here's a `blog post where Derek's
created an image`_ that you can simply dd on to your USB. It worked like
a charm.

In a sentence: download the image, extract it from the bz2 archive, dd
it to your pen drive, copy the BIOS exe file to it, reboot, run the BIOS
update.

Simple isn't it? Yup.

.. _latest version that Dell provides me: http://www.dell.com/support/drivers/us/en/19/DriverDetails/Product/vostro-3400?driverId=6W3H0&fileId=2731099204&osCode=BIOSA#OldVersion
.. _that Adam suggested in this bug report: https://bugzilla.redhat.com/show_bug.cgi?id=832679
.. _System Rescue CD: http://www.sysresccd.org/Sysresccd-manual-en_How_to_install_SystemRescueCd_on_an_USB-stick
.. _try and use it directly with Grub2: http://www.sysresccd.org/Sysresccd-manual-en_Easy_install_SystemRescueCd_on_harddisk#Boot_the_ISO_image_from_the_disk_using_Grub2
.. _FreeDOS: http://www.freedos.org/download/
.. _blog post where Derek's created an image: http://derek.chezmarcotte.ca/?p=188
