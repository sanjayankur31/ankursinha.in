Scripting in Scribus
####################
:date: 2015-06-26 14:59:08
:author: ankur
:category: Tech
:tags: Fedora, Scribus
:slug: scripting-in-scribus
:summary: I was looking at automating the creation of some documents and spent sometime discovering how one can use the scripting feature in Scribus. This post summarises some of what I found.

Scribus_ is a well known tool that quite a few people use for creating documents. One of the more useful features in Scribus is the `scripting support`_. I had quite a silly task at hand - we have some A5 forms that need to be filled in each month. I wanted to see if I could automate this somehow and ended up looking into Scribus. The documentation on scripting, while present, is quite difficult to learn from. The `API documentation`_ that they have isn't quite complete either from what I saw. I spent a couple of hours tinkering with it, and did manage to get my work done. This is how I got around to it:

Use the console
---------------

The best source of documentation is the Scribus scripting console itself (Script -> Show console). For example, if you want to get a list of all constants and functions available to you:

.. code-block:: python

    from scribus import *
    dir(scribus)

    ['%', 'ALIGN_BLOCK', 'ALIGN_CENTERED', 'ALIGN_FORCED', 'ALIGN_LEFT', 'ALIGN_RIGHT', 'BUTTON_ABORT', 'BUTTON_CANCEL', 'BUTTON_IGNORE', 'BUTTON_NO', 'BUTTON_NONE', 'BUTTON_OK', 'BUTTON_RETRY', 'BUTTON_YES', 'CAP_FLAT', 'CAP_ROUND', 'CAP_SQUARE', 'COLOR', 'COLOR_BURN', 'COLOR_DODGE', 'DARKEN', 'DIFFERENCE', 'EXCLUSION', 'FACINGPAGES', 'FILL_CROSSDIAGONALG', 'FILL_DIAGONALG', 'FILL_HORIZONTALG', 'FILL_NOG', 'FILL_RADIALG', 'FILL_VERTICALG', 'FIRSTPAGELEFT', 'FIRSTPAGERIGHT', 'HARD_LIGHT', 'HUE', 'ICON_CRITICAL', 'ICON_INFORMATION', 'ICON_NONE', 'ICON_WARNING', 'ImageExport', 'JOIN_BEVEL', 'JOIN_MITTER', 'JOIN_ROUND', 'LANDSCAPE', 'LIGHTEN', 'LINE_DASH', 'LINE_DASHDOT', 'LINE_DASHDOTDOT', 'LINE_DOT', 'LINE_SOLID', 'LUMINOSITY', 'MULTIPLY', 'NOFACINGPAGES', 'NORMAL', 'NameExistsError', 'NoDocOpenError', 'NoValidObjectError', 'NotFoundError', 'OVERLAY', 'PAGE_1', 'PAGE_2', 'PAGE_3', 'PAGE_4', 'PAPER_A0', 'PAPER_A1', 'PAPER_A2', 'PAPER_A3', 'PAPER_A4', 'PAPER_A5', 'PAPER_A6', 'PAPER_A7', 'PAPER_A8', 'PAPER_A9', 'PAPER_B0', 'PAPER_B1', 'PAPER_B10', 'PAPER_B2', 'PAPER_B3', 'PAPER_B4', 'PAPER_B5', 'PAPER_B6', 'PAPER_B7', 'PAPER_B8', 'PAPER_B9', 'PAPER_C5E', 'PAPER_COMM10E', 'PAPER_DLE', 'PAPER_EXECUTIVE', 'PAPER_FOLIO', 'PAPER_LEDGER', 'PAPER_LEGAL', 'PAPER_LETTER', 'PAPER_TABLOID', 'PDFfile', 'PORTRAIT', 'Printer', 'SATURATION', 'SCREEN', 'SOFT_LIGHT', 'ScribusException', 'UNIT_C', 'UNIT_CENTIMETRES', 'UNIT_CICERO', 'UNIT_CM', 'UNIT_IN', 'UNIT_INCHES', 'UNIT_MILLIMETERS', 'UNIT_MM', 'UNIT_P', 'UNIT_PICAS', 'UNIT_POINTS', 'UNIT_PT', 'WrongFrameTypeError', '__builtin__', '__doc__', '__name__', '__package__', '_bu', '_ia', 'applyMasterPage', 'c', 'changeColor', 'closeDoc', 'closeMasterPage', 'cm', 'createBezierLine', 'createCharStyle', 'createEllipse', 'createImage', 'createLayer', 'createLine', 'createMasterPage', 'createParagraphStyle', 'createPathText', 'createPolyLine', 'createPolygon', 'createRect', 'createText', 'currentPage', 'defineColor', 'dehyphenateText', 'deleteColor', 'deleteLayer', 'deleteMasterPage', 'deleteObject', 'deletePage', 'deleteText', 'deselectAll', 'docChanged', 'duplicateObject', 'editMasterPage', 'exceptions', 'fileDialog', 'fileQuit', 'getActiveLayer', 'getAllObjects', 'getAllStyles', 'getAllText', 'getColor', 'getColorAsRGB', 'getColorNames', 'getColumnGap', 'getColumns', 'getCornerRadius', 'getDocName', 'getFillBlendmode', 'getFillColor', 'getFillShade', 'getFillTransparency', 'getFont', 'getFontNames', 'getFontSize', 'getGuiLanguage', 'getHGuides', 'getImageFile', 'getImageScale', 'getLayerBlendmode', 'getLayerTransparency', 'getLayers', 'getLineBlendmode', 'getLineCap', 'getLineColor', 'getLineJoin', 'getLineShade', 'getLineSpacing', 'getLineStyle', 'getLineTransparency', 'getLineWidth', 'getObjectType', 'getPageItems', 'getPageMargins', 'getPageNMargins', 'getPageNSize', 'getPageSize', 'getPageType', 'getPosition', 'getProperty', 'getPropertyCType', 'getPropertyNames', 'getRotation', 'getSelectedObject', 'getSize', 'getText', 'getTextColor', 'getTextDistances', 'getTextLength', 'getTextLines', 'getTextShade', 'getUnit', 'getVGuides', 'getXFontNames', 'getval', 'gotoPage', 'groupObjects', 'haveDoc', 'hyphenateText', 'importPage', 'inch', 'insertText', 'isLayerFlow', 'isLayerLocked', 'isLayerOutlined', 'isLayerPrintable', 'isLayerVisible', 'isLocked', 'isPDFBookmark', 'isSpotColor', 'linkTextFrames', 'loadImage', 'loadStylesFromFile', 'lockObject', 'mainWindow', 'masterPageNames', 'messageBox', 'messagebarText', 'mm', 'moveObject', 'moveObjectAbs', 'moveSelectionToBack', 'moveSelectionToFront', 'newDoc', 'newDocDialog', 'newDocument', 'newPage', 'newStyleDialog', 'objectExists', 'openDoc', 'p', 'pageCount', 'pageDimension', 'placeEPS', 'placeODG', 'placeSVG', 'placeSXD', 'progressReset', 'progressSet', 'progressTotal', 'pt', 'qApp', 'redrawAll', 'renderFont', 'replaceColor', 'retval', 'rotateObject', 'rotateObjectAbs', 'saveDoc', 'saveDocAs', 'savePageAsEPS', 'scaleGroup', 'scaleImage', 'scribus_version', 'scribus_version_info', 'scrollDocument', 'selectObject', 'selectText', 'selectionCount', 'sentToLayer', 'setActiveLayer', 'setColumnGap', 'setColumns', 'setCornerRadius', 'setCursor', 'setDocType', 'setFillBlendmode', 'setFillColor', 'setFillShade', 'setFillTransparency', 'setFont', 'setFontSize', 'setGradientFill', 'setGradientStop', 'setHGuides', 'setImageOffset', 'setImageScale', 'setInfo', 'setLayerBlendmode', 'setLayerFlow', 'setLayerLocked', 'setLayerOutlined', 'setLayerPrintable', 'setLayerTransparency', 'setLayerVisible', 'setLineBlendmode', 'setLineCap', 'setLineColor', 'setLineJoin', 'setLineShade', 'setLineSpacing', 'setLineStyle', 'setLineTransparency', 'setLineWidth', 'setMargins', 'setMultiLine', 'setNewName', 'setPDFBookmark', 'setProperty', 'setRedraw', 'setScaleImageToFrame', 'setSpotColor', 'setStyle', 'setText', 'setTextAlignment', 'setTextColor', 'setTextDistances', 'setTextScalingH', 'setTextScalingV', 'setTextShade', 'setTextStroke', 'setUnit', 'setVGuides', 'sizeObject', 'statusMessage', 'textFlowMode', 'textOverflows', 'traceText', 'unGroupObject', 'unlinkTextFrames', 'valueDialog', 'warnings', 'zoomDocument', '\xb0']

Then, use the built-in help method to find out how to use these methods:

.. code-block:: python

    from scribus import *
    help(newDoc)

    Help on built-in function newDocument in module scribus:

    newDocument(...)
        newDocument(size, margins, orientation, firstPageNumber, unit, pagesType, firstPageOrder, numPages) -> bool
        Creates a new document and returns true if successful. The parameters have the following meaning:
        size = A tuple (width, height) describing the size of the document. You can use predefined constants named PAPER_<paper_type> e.g. PAPER_A4 etc.
        margins = A tuple (left, right, top, bottom) describing the document margins
        orientation = the page orientation - constants PORTRAIT, LANDSCAPE
        firstPageNumer = is the number of the first page in the document used for pagenumbering. While you'll usually want 1, it's useful to have higher numbers if you're creating a document in several parts.
        unit: this value sets the measurement units used by the document. Use a predefined constant for this, one of: UNIT_INCHES, UNIT_MILLIMETERS, UNIT_PICAS, UNIT_POINTS.
        pagesType = One of the predefined constants PAGE_n. PAGE_1 is single page, PAGE_2 is for double sided documents, PAGE_3 is for 3 pages fold and PAGE_4 is 4-fold.

        firstPageOrder = What is position of first page in the document. Indexed from 0 (0 = first).
        numPage = Number of pages to be created.
        The values for width, height and the margins are expressed in the given unit for the document. PAPER_* constants are expressed in points. If your document is not in points, make sure to account for this.
    
        example: newDocument(PAPER_A4, (10, 10, 20, 20), LANDSCAPE, 7, UNIT_POINTS, PAGE_4, 3, 1)
    
        May raise ScribusError if is firstPageOrder bigger than allowed by pagesType.


The work flow
-------------

In general, you basically follow the same work flow as you would when using the UI. For example, `here is the script I wrote`_. It reads information from a file and creates pages with this data:

.. code-block:: bash

    July 2015

    Name 1
    ID 1

    Name 2
    ID 2

.. code-block:: python

    from scribus import *

    # Create a new document with the required sizes, orientation, margins and so on.
    if newDocument((148,210), (10,10,10,10), LANDSCAPE, 1, UNIT_MM, NOFACINGPAGES, FIRSTPAGERIGHT, 1):
        # Some constants required to place my text
        spx=142
        spy=29 + 4
        width=57
        height=9.5

        # Oh look! A select file dialog!
        selectfile = fileDialog("Select file")
        # Open the file
        file = open (selectfile,"r")

        # Read the first line
        date_year = file.readline()
        date_year = date_year.rstrip('\n')

        while 1:
            name = file.readline()
            number = file.readline()

            if not name:
                break

            if name == '\n':
                continue

            name = name.rstrip('\n')
            number = number.rstrip('\n')

            # A text box
            name_box = createText(spx,spy,width,height)
            # Add some text to the box
            setText(name, name_box)
            # Modify the text properties
            setTextAlignment(ALIGN_CENTERED, name_box)
            setFont("DejaVu Sans Book", name_box)
            setFontSize(13, name_box)
            setLineWidth(0, name_box)

            number_box = createText(spx,(spy+height),width,height)
            setText(number, number_box)
            setTextAlignment(ALIGN_CENTERED, number_box)
            setFont("DejaVu Sans Book", number_box)
            setFontSize(13, number_box)
            setLineWidth(0, number_box)

            month_box = createText(spx,(spy+(2*height)),width,height)
            setText(date_year, month_box)
            setTextAlignment(ALIGN_CENTERED, month_box)
            setFont("DejaVu Sans Book", month_box)
            setFontSize(13, month_box)
            setLineWidth(0, month_box)

            # Create a new page
            newPage(-1)
            name = ''
            number = ''

        # Save the document
        saveDocAs("blue-cards-" + date_year + ".sla")

Of course, you can do a lot more - you'll have to look at the documentation and some example scripts to get a hang of it. Be careful when looking at the examples though, they may not all be up to date. Since you can use pure python methods and so on, the scripting support lets you automate all sorts of tasks - create flyers and brochures and so on. `Here's a list of things made with Scribus`_ - you can set up the layout manually and then supply the text from files using a script, for example.

A last note - Scribus isn't visible in Gnome Software at the moment - the icon size is too small. There's a `bug filed about this already`_. You'll have to use the command line to install it:

.. code-block:: bash

    sudo dnf install scribus

Cheers!

.. _bug filed about this already: https://bugzilla.redhat.com/show_bug.cgi?id=1231445
.. _Here's a list of things made with Scribus: http://wiki.scribus.net/canvas/Made_with_Scribus#English
.. _Scribus: http://www.scribus.net/
.. _scripting support: http://wiki.scribus.net/canvas/Category:Scripts
.. _API documentation: http://scribus-scripter.readthedocs.org/en/latest/
.. _here is the script I wrote: https://github.com/sanjayankur31/scribus-blue-cards/blob/master/generate-blue-cards.py


