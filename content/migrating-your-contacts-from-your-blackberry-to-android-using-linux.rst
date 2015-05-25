Migrating your contacts from your Blackberry to Android using Linux
###################################################################
:date: 2012-06-30 00:41
:author: ankur
:category: Tech
:tags: Fedora
:slug: migrating-your-contacts-from-your-blackberry-to-android-using-linux

I got my father an Android today: an HTC Explorer. (The Blackberry 3G
plans here in India are too expensive). Of course, he had years of
contacts built up in his Blackberry and I needed to migrate them. Here's
how I did it:

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

1. Install barry
::

    # yum install barry

.. raw:: html

   </div>

.. raw:: html

   <div>

2. Connect the Blackberry and run the command:

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

::

    btool -V -d "Address Book" > dadcontacts.vcf #dump contacts in vcard format

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

3. I then imported these on to his Google contacts, merged and deleted
dups, and synced his phone. Of course, you can also copy the vcf to your
memory card and import it if you don't want to go via Google.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

That's all. Have fun!

.. raw:: html

   </div>

