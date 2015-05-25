if sealert is still broken for you
##################################
:date: 2011-07-04 08:13
:author: ankur
:category: Tech
:tags: Fedora
:slug: if-sealert-is-still-broken-for-you

Hi!!

If any of you are still seeing this error on running sealert after the
latest updates :

::

    Traceback (most recent call last):
      File "/usr/bin/sealert", line 692, in <module>
        run_as_dbus_service(username)
      File "/usr/bin/sealert", line 112, in run_as_dbus_service
        app = SEAlert(user, dbus_service.presentation_manager,
    watch_setroubleshootd=True)
      File "/usr/bin/sealert", line 326, in __init__
        from setroubleshoot.browser import BrowserApplet
      File "/usr/lib64/python2.7/site-packages/setroubleshoot/browser.py", line 46,
    in <module>
        import report.io.GTKIO
    ImportError: No module named GTKIO

,

please install report-gtk :

::

     yum install report-gtk 

That should fix it.
