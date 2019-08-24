#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     TT-Site2019-08.py
#
import os
import shutil
import webbrowser

from pagebot.publications.publication import Publication
from pagebot.constants import URL_JQUERY, LANGUAGE_EN
from pagebot.composer import Composer
from pagebot.typesetter import Typesetter
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.toolbox.color import color, whiteColor, blackColor, spotColor
from pagebot.toolbox.units import em, pt
from pagebot.elements.web.nanosite.siteelements import *

from css.ttstyle_css import cssPy

from pagebot.themes import *
#   BackToTheCity
#   BusinessAsUsual 
#   FairyTales 
#   FreshAndShiny 
#   IntoTheWoods 
#   SeasoningTheDish 
#   SomethingInTheAir 
#   WordlyWise
#   HappyHolidays

MLFT_LOGO = color(0.2, 0.4, 0.1)

class MLFTTheme(BaseTheme):
    NAME = 'MLFT'
    BASE_COLORS = dict(
        base1=color(1, 0, 0),
        base2=color('#ACACB8'),
        base3=MLFT_LOGO,
        logo=MLFT_LOGO,
    )

theme = MLFTTheme('light')

SITE_NAME = 'TYPE-TRY' # Also used as logo

MD_PATHS = [
    'TT-home.md',
    'TT-upgrade.md',
    #'TT-upgrade-cjk.md',
    'TT-bitcount.md',
    'TT-powerlift.md',
    'TT-prominence.md',
    #'TT-promise.md',
    'TT-contact.md',
]
EXPORT_PATH = '_export/' + SITE_NAME # Export path for DO_FILE

FONT_DATA_LIST = {
    'Upgrade': [ 
        ('Upgrade-Book', dict(
            download='font/Upgrade_Try.zip',
            seeAlso='https://upgrade.typenetwork.com',
            adobe='https://fonts.adobe.com/fonts/upgrade',
            typenetwork='https://store.typenetwork.com/foundry/typetr/fonts/upgrade',
        )),
        ('Upgrade-Regular', dict(
            download='font/Upgrade_Try.zip',
            seeAlso='https://upgrade.typenetwork.com',
            adobe='https://fonts.adobe.com/fonts/upgrade',
            typenetwork='https://store.typenetwork.com/foundry/typetr/fonts/upgrade',
        )),
        ('Upgrade-Medium', dict(
            download='font/Upgrade_Try.zip',
            seeAlso='https://upgrade.typenetwork.com',
            adobe='https://fonts.adobe.com/fonts/upgrade',
            typenetwork='https://store.typenetwork.com/foundry/typetr/fonts/upgrade',
        )),
        ('Upgrade-Semibold', dict(
            download='font/Upgrade_Try.zip',
            seeAlso='https://upgrade.typenetwork.com',
            adobe='https://fonts.adobe.com/fonts/upgrade',
            typenetwork='https://store.typenetwork.com/foundry/typetr/fonts/upgrade',
        )),
        ('Upgrade-Bold', dict(
            download='font/Upgrade_Try.zip',
            seeAlso='https://upgrade.typenetwork.com',
            adobe='https://fonts.adobe.com/fonts/upgrade',
            typenetwork='https://store.typenetwork.com/foundry/typetr/fonts/upgrade',
        )),
    ],
    'PowerLift': [
        ('PowerLift-Tight', dict(
            download='font/PowerLift_Try.zip',
            adobe='https://fonts.adobe.com/fonts/powerlift',
            typenetwork='https://store.typenetwork.com/foundry/typetr/fonts/powerlift',
        )),
        ('PowerLift-Tight_Outline', dict(
            download='font/PowerLift_Try.zip',
            adobe='https://fonts.adobe.com/fonts/powerlift',
            typenetwork='https://store.typenetwork.com/foundry/typetr/fonts/powerlift',
        )),
    ],
    'Bitcount Outline Round': [
        ('Bitcount_Try_Mono_Double_Outline-Black_Round', dict(
            sample='Bitcount Black Round',
            seeAlso='https://bitcount.typenetwork.com',
            typenetwork='https://store.typenetwork.com/foundry/typetr/fonts/bitcount',
        )),
        ('Bitcount_Try_Mono_Double_Outline-ExtraBold_Round', dict(
            sample='Bitcount X-Bold Round',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Bold_Round', dict(
            sample='Bitcount Bold Round',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Medium_Round', dict(
            sample='Bitcount Medium Round',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Round', dict(
            sample='Bitcount (Regular) Round',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Book_Round', dict(
            sample='Bitcount Book Round',
        )),
    ],
    'Bitcount Outline Square': [
        ('Bitcount_Try_Mono_Double_Outline-Black_Square', dict(
            sample='Bitcount Black Square',
        )),
        ('Bitcount_Try_Mono_Double_Outline-ExtraBold_Square', dict(
            sample='Bitcount X-Bold Square',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Bold_Square', dict(
            sample='Bitcount Bold Square',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Medium_Square', dict(
            sample='Bitcount Medium Square',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Square', dict(
            sample='Bitcount (Regular) Square',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Book_Square', dict(
            sample='Bitcount Book Square',
        )),
    ],
    'Bitcount Outline Square Italic': [
        ('Bitcount_Try_Mono_Double_Outline-Black_Square_Italic', dict(
            sample='Bitcount Black Sq.Italic',
        )),
        ('Bitcount_Try_Mono_Double_Outline-ExtraBold_Square_Italic', dict(
            sample='Bitcount X-Bold Sq.Italic',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Bold_Square_Italic', dict(
            sample='Bitcount Bold Sq.Italic',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Medium_Square_Italic', dict(
            sample='Bitcount Medium Sq.Italic',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Square_Italic', dict(
            sample='Bitcount (Regular) Sq.Italic',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Book_Square_Italic', dict(
            sample='Bitcount Book Sq.Italic',
        )),
    ],

}

VERBOSE = False
DO_SPELLCHECK = False

DO_PDF = 'Pdf' # Save as PDF representation of the site.
DO_FILE = 'File' # Generate website output in _export/SimpleSite and open browser on file index.html
DO_MAMP = 'Mamp' # Generate website in /Applications/Mamp/htdocs/SimpleSite and open a localhost
DO_GIT = 'Git' # Generate website and commit to git (so site is published in git docs folder.
EXPORT_TYPE = DO_MAMP

CLEAR_MAMP = False # If True, make a clean copy by removing all old files first.

NUM_CONTENT = 2 # Number of content elements on a page.
NUM_SIDES = 1 # Number of side elements next to a main content element,

# Max image size of scaled cache (used mulitplied by resolution per image type DEFAULT_RESOLUTION_FACTORS
MAX_IMAGE_WIDTH = 800 


styles = dict(
    body=dict(
        fill=whiteColor,
        ml=9, mr=0, mt=0, mb=0,
        pl=em(3), pr=em(3), pt=em(3), pb=em(3),
        fontSize=pt(12),
        leading=em(1.4),
    ),
    br=dict(leading=em(1.4)
    ),
)

def makeNavigation(doc):
    """After all pages of the site are generated, we can use the compiled page tree
    from doc to let all Navigation elements build the menu for each page.
    """
    for pages in doc.pages.values():
        for page in pages:  
            navigation = page.select('Navigation')
            if navigation is not None:
                navigation.pageTree = doc.getPageTree() # Get a fresh one for each page

def makeTemplate(doc):

    # D E F A U L T

    default = Template('Default', context=doc.context)
    wrapper = Wrapper(parent=default) # Create main page wrapper
    
    header = Header(parent=wrapper) # Header to hold logo and navigation elements

    #logoString = doc.context.newString(SITE_NAME)
    Logo(parent=header, url='images/TYPE-TRY-logo.gif')
    BurgerButton(parent=header)

    # Responsive conditional menus
    Navigation(parent=header)
    MobileMenu(parent=header)

    # Just make a simple content container in this template.
    # Rest of content is created upon request in MarkDown
    Content(parent=wrapper) 

    # Default Footer at bottom of every page.
    Footer(parent=wrapper)

    doc.addTemplate('default', default)
    return default

def makeSite(styles, viewId):
    site = Site(styles=styles)
    doc = site.newDocument(viewId=viewId, name='TYPE-TRY', autoPages=1, defaultImageWidth=MAX_IMAGE_WIDTH)
    
    doc.docLib['fontDataList'] = FONT_DATA_LIST

    doc.theme = theme

    view = doc.view
    # Directories that need to be copies. "images" probably includes 
    # "images/_scaled" directory that needs to be copied too.
    # If using Github/docs as site, then remoce "_scaled" from .gitignore
    # in order to commit the scaled images as well.
    view.resourcePaths = ('css', 'fonts', 'downloads', 'images', 'js')
    view.jsUrls = (
        URL_JQUERY, 
        'js/jquery.bbslider.min.js',
        #URL_MEDIA, 
        #'js/sitemain.js', 
    )
    
    # Generate css by mapping theme.mood on cssPy 
    cssPath = 'css/ttstyle_py.css'
    doc.context.b.writeCss(cssPath, cssPy % theme.mood)

    view.cssUrls = (
        'css/jquery.bbslider.css',
        'fonts/webfonts.css', 
        'css/normalized.css', 
        cssPath,
    )
    BASE_FONT_SIZE = 16
    view.jsCode = """
    function setBaseFontSize(){
        /*document.getElementsByTagName('body')[0].style['font-size'] = %d * window.devicePixelRatio + 'px';*/
    }
    window.onload = setBaseFontSize;
    """ % BASE_FONT_SIZE

    # Make the all pages and elements of the site as empty containers, that then can
    # be selected and filled by the composer, using the galley content.
    # Of the MarkDown text can decide to create new elements inside selected elements.
    template = makeTemplate(doc)    

    page = doc[1]
    page.applyTemplate(template) # Copy element tree to page.

    # By default, the typesetter produces a single Galley with content and code blocks.    
    t = Typesetter(doc.context)
    for mdPath in MD_PATHS:
        t.typesetFile(mdPath)
    
    # Create a Composer for this document, then create pages and fill content. 
    composer = Composer(doc)

    # The composer executes the embedded Python code blocks that indicate where content should go.
    # by the HtmlContext. Feedback by the code blocks is added to verbose and errors list
    targets = dict(doc=doc, page=page, template=template)
    composer.compose(t.galley, targets=targets)

    if VERBOSE:
        if targets['verbose']:
            print('Verbose\n', '\n'.join(targets['verbose']))
        # In case there are any errors, show them.
        if targets['errors']:
            print('Errors\n', '\n'.join(targets['errors']))
    
    # Find the navigation elements and fill them, now we know all the pages.
    makeNavigation(doc)

    # https://www.hyphenator.net/en/word/...
    if DO_SPELLCHECK:
        unknownWords = doc.spellCheck(LANGUAGE_EN)
        if unknownWords:
            print(unknownWords)

    return doc

if EXPORT_TYPE == DO_PDF: # PDF representation of the site
    doc = makeSite(styles=styles, viewId='Page')
    doc.solve() # Solve all layout and float conditions for pages and elements.
    doc.export(EXPORT_PATH + '.pdf')

elif EXPORT_TYPE == DO_FILE:
    doc = makeSite(styles=styles, viewId='Site')
    doc.export(EXPORT_PATH)
    openingPage = 'program-2019.html'
    os.system(u'/usr/bin/open "%s/%s"' % (EXPORT_PATH, openingPage))

elif EXPORT_TYPE == DO_MAMP:
    # Internal CSS file may be switched off for development.
    doc = makeSite(styles=styles, viewId='Mamp')
    mampView = doc.view
    MAMP_PATH = '/Applications/MAMP/htdocs/' 
    filePath = MAMP_PATH + SITE_NAME 
    if VERBOSE:
        print('Site path: %s' % MAMP_PATH)
    if os.path.exists(filePath):
        shutil.rmtree(filePath) # Comment this line, if more safety is required. In that case manually delete.
    print('Doc pages: %d' % len(doc))
    doc.export(filePath)

    if not os.path.exists(filePath):
        print('The local MAMP server application does not exist. Download and install from %s.' % view.MAMP_SHOP_URL)
        os.system(u'/usr/bin/open %s' % view.MAMP_SHOP_URL)
    else:
        #t.doc.export('_export/%s.pdf' % NAME, multiPages=True)
        os.system(u'/usr/bin/open "%s"' % mampView.getUrl(SITE_NAME))

elif EXPORT_TYPE == DO_GIT: # Not supported for SimpleSite, only one per repository?
    # Make sure outside always has the right generated CSS
    doc = makeSite(styles=styles, viewId='Git')
    gitView = doc.view
    GIT_PATH = 'docs/' 
    if VERBOSE:
        print('Site path: %s' % MAMP_PATH)
    #if os.path.exists(filePath):
    #    shutil.rmtree(filePath) # Comment this line, if more safety is required. In that case manually delete.
    doc.export(GIT_PATH)

    # Open the css file in the default editor of your local system.
    if 0:
        os.system('/usr/bin/git pull')
        os.system('/usr/bin/git add *')
        os.system('/usr/bin/git commit -m "Updating website changes."')
        os.system('/usr/bin/git pull')
        os.system('/usr/bin/git push')
        #os.system(u'/usr/bin/open "%s"' % gitView.getUrl(DOMAIN))

else: # No output view defined
    print('Set EXPORTTYPE to DO_FILE or DO_MAMP or DO_GIT')

