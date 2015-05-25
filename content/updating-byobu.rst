Updating byobu
##############
:date: 2012-04-25 14:38
:author: ankur
:category: Tech
:tags: Fedora
:slug: updating-byobu

`Byobu`_ in fedora hasn't been updated in a while. The current fedora
version is **4.4**, while upstream has moved on to **5.17**. That's
quite a lag we have. There's a `bug filed requesting an update`_ by
`Upstream release monitoring`_, but it hasn't received any human
responses at all! It was filed in October 2011. Since I use byobu, 24x7,
I've gone ahead and taken the initiative to update the package and
submit the `spec`_\ to the maintainer in the bug. I hope to see it
updated soon. I've done a `scratch build`_, you can use the noarch
package if you are in a hurry like me. The srpm is available `here`_, so
you can build it for your fedora version too.

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

I'm not well versed with byobu internals really, so if you do find any
issues with the updated package, please comment on the bug and let the
maintainer know. 

.. raw:: html

   </div>

.. _Byobu: https://launchpad.net/byobu
.. _bug filed requesting an update: https://bugzilla.redhat.com/show_bug.cgi?id=748127
.. _Upstream release monitoring: https://fedoraproject.org/wiki/Upstream_release_monitoring
.. _spec: https://bugzilla.redhat.com/attachment.cgi?id=580100
.. _scratch build: http://koji.fedoraproject.org/koji/taskinfo?taskID=4021403
.. _here: http://ankursinha.fedorapeople.org/byobu/byobu-5.17-1.fc17.src.rpm
