My adventures with Packaging.. I'm Stuck :(
###########################################
:date: 2009-05-10 21:06
:author: ankur
:category: FOSS
:tags: Fedo, Fedora, packaging
:tags: Fedo, Fedora, packaging
:tags: Fedo, Fedora, packaging
:tags: Fedo, Fedora, packaging
:slug: my-adventures-with-packaging-im-stuck-2

Well.. Here it is.. Good and bad news.. The packaging went smoothly..
The spec is correct, so are the rpms. No rpmlint errors at all.. But,
here's the catch :

Everytime I try to run the app. I get this error load. The terminal
just blinks here until I Ctrl+ it.

..code-block:: bash

    Ankur@Ankur twitter\_tui]$ panini
    Locking assertion failure. Backtrace:
    #0 /usr/lib/libxcb-xlib.so.0 [0xf09767]
    #1 /usr/lib/libxcb-xlib.so.0(xcb\_xlib\_lock+0x2e) [0xf0990e]
    #2 /usr/lib/libX11.so.6 [0x5a90e9]
    #3 /usr/lib/libX11.so.6(XCreateSimpleWindow+0x26) [0x57edb6]
    #4 /usr/lib/libQtGui.so.4 [0x72c3c85]
    #5
    /usr/lib/libQtGui.so.4(\_ZN14QWidgetPrivate10create\_sysEmbb+0x1828)
    [0x72c25d8]
    #6 /usr/lib/libQtGui.so.4(\_ZN7QWidget6createEmbb+0x16c)
    [0x7284c1c]
    #7
    /usr/lib/libQtGui.so.4(\_ZN14QWidgetPrivate11createWinIdEm+0x1e3)
    [0x727ff43]
    #8
    /usr/lib/libQtGui.so.4(\_ZN14QWidgetPrivate21setWindowTitle\_helperERK7QString+0x9b)
    [0x72845bb]
    #9
    /usr/lib/libQtGui.so.4(\_ZN7QWidget14setWindowTitleERK7QString+0xa2)
    [0x7284a12]
    #10
    /usr/lib/libQtGui.so.4(\_ZN11QMessageBox14setWindowTitleERK7QString
    +0x24) [0x7766554]
    #11 /usr/lib/libQtGui.so.4 [0x7768237]
    #12
    /usr/lib/libQtGui.so.4(\_ZN11QMessageBoxC1ENS\_4IconERK7QStringS3\_6QFlagsINS\_14StandardButtonEEP7QWidgetS4\_IN2Qt10WindowTypeEE+0x1f0)
    [0x77685b0]
    #13 /usr/lib/libQtGui.so.4 [0x776885b]
    #14
    /usr/lib/libQtGui.so.4(\_ZN11QMessageBox7warningEP7QWidgetRK7QStringS4\_6QFlagsINS\_14StandardButtonEES6\_+0x36)
    [0x7768a76]
    #15 panini [0x8057ca3]
    #16
    /usr/lib/libQtCore.so.4(\_Z17qt\_message\_output9QtMsgTypePKc+0x35)
    [0x6f0d095]
    #17 /usr/lib/libQtCore.so.4(\_Z8qWarningPKcz+0x71) [0x6f0d431]
    #18 /usr/lib/libQtGui.so.4 [0x7290268]
    #19 /usr/lib/libX11.so.6(\_XError+0x109) [0x5a1aa9]
    ^Quit
    [Ankur@Ankur twitter\_tui]$

Searching the net gave me quite a few results, most of them centered
around java and matlab on Ubuntu. Their solutions din't work for me..I'm
going to keep looking.. In the meantime..  Any ideas anyone?? I'm
waiting on the devel list for help here..

Here are all the files I found..Logs, the rpms..

http://ankursinha.fedorapeople.org/panini/
