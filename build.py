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
#     build.py
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

VERBOSE = False
DO_SPELLCHECK = False

DO_PDF = 'Pdf' # Save as PDF representation of the site.
DO_FILE = 'File' # Generate website output in _export/SimpleSite and open browser on file index.html
DO_MAMP = 'Mamp' # Generate website in /Applications/Mamp/htdocs/SimpleSite and open a localhost
DO_GIT = 'Git' # Generate website and commit to git (so site is published in git docs folder.
EXPORT_TYPE = DO_MAMP

CLEAR_MAMP = False # If True, make a clean copy by removing all old files first.

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

# Template for email to by a license direct from TYPETR.
# Use as BUY_BY_EMAIL % dict(familyName='Family name')
BUY_SUBJECT = 'License for TYPETR-%(familyName)s'
BUY_BY_BODY = 'Dear TYPETR, please send info about licensing %(familyName)s styles, intended to be used for ...'
BUY_BY_EMAIL = 'mailto:info@typetr.com?subject='+BUY_SUBJECT+'&body='+BUY_BY_BODY

SITE_NAME = 'TYPE-TRY' # Also used as logo

MD_PATHS = [
    'TT-home.md',
    'TT-bitcount.md',
    'TT-opcode.md',
    'TT-presti.md',
    'TT-powerlift.md',
    'TT-prominence.md',
    'TT-promise.md',
    'TT-responder.md',
    'TT-stickway.md',
    'TT-upgrade.md',
    #'TT-upgrade-cjk.md',
    'TT-other.md',
    'TT-contact.md',
]
EXPORT_PATH = '_export/' + SITE_NAME # Export path for DO_FILE

FONT_DATA_LIST = {
    'Upgrade': [ 
        ('Upgrade-Thin', dict(
        )),
        ('Upgrade-Light', dict(
        )),
        ('Upgrade-Book', dict(
        )),
        ('Upgrade-Regular', dict(
        )),
        ('Upgrade-Medium', dict(
         )),
        ('Upgrade-Semibold', dict(
        )),
        ('Upgrade-Bold', dict(
            download='downloads/TYPETR-Upgrade_Try.zip',
            seeAlso='https://upgrade.typenetwork.com',
            adobe='https://fonts.adobe.com/fonts/upgrade',
            typenetwork='https://store.typenetwork.com/foundry/typetr/fonts/upgrade',
            #google='https://www.google.com/search?q=typetr+upgrade+usage&oq=typetr+upgrade+usage',
            buybyemail=BUY_BY_EMAIL % dict(familyName='Upgrade'),
        )),
    ],
    'Upgrade Try': [
        ('Upgrade_Try-Hairline', dict()),
        ('Upgrade_Try-Thin', dict()),
        ('Upgrade_Try-ExtraLight', dict()),
        ('Upgrade_Try-Light', dict()),
        ('Upgrade_Try-Cover', dict()),
        ('Upgrade_Try-Book', dict()),
        ('Upgrade_Try-Normal', dict()),
        ('Upgrade_Try-Regular', dict()),
        ('Upgrade_Try-Standard', dict()),
        ('Upgrade_Try-Medium', dict()),
        ('Upgrade_Try-Semibold', dict()),
        ('Upgrade_Try-Bold', dict()),
        ('Upgrade_Try-Black', dict()),
        ('Upgrade_Try-ExtraBlack', dict()),
        ('Upgrade_Try-UltraBlack', dict(
            download='downloads/TYPETR_Upgrade_Try-ttf.zip',
            seeAlso='https://upgrade.typenetwork.com',
            adobe='https://fonts.adobe.com/fonts/upgrade',
            typenetwork='https://store.typenetwork.com/foundry/typetr/fonts/upgrade',
            #google='https://www.google.com/search?q=typetr+upgrade+usage&oq=typetr+upgrade+usage',
            buybyemail=BUY_BY_EMAIL % dict(familyName='Upgrade'),
        )),
    ],
    'Upgrade Try Italic': [
        ('Upgrade_Try-Hairline_Italic', dict()),
        ('Upgrade_Try-Thin_Italic', dict()),
        ('Upgrade_Try-ExtraLight_Italic', dict()),
        ('Upgrade_Try-Light_Italic', dict()),
        ('Upgrade_Try-Cover_Italic', dict()),
        ('Upgrade_Try-Book_Italic', dict()),
        ('Upgrade_Try-Normal_Italic', dict()),
        ('Upgrade_Try-Italic', dict()),
        ('Upgrade_Try-Standard_Italic', dict()),
        ('Upgrade_Try-Medium_Italic', dict()),
        ('Upgrade_Try-Semibold_Italic', dict()),
        ('Upgrade_Try-Bold_Italic', dict()),
        ('Upgrade_Try-Black_Italic', dict()),
        ('Upgrade_Try-ExtraBlack_Italic', dict()),
        ('Upgrade_Try-UltraBlack_Italic', dict(
            download='downloads/TYPETR-Upgrade_Try-italic_ttf.zip',
            seeAlso='https://upgrade.typenetwork.com',
            adobe='https://fonts.adobe.com/fonts/upgrade',
            typenetwork='https://store.typenetwork.com/foundry/typetr/fonts/upgrade',
            #google='https://www.google.com/search?q=typetr+upgrade+usage&oq=typetr+upgrade+usage',
            buybyemail=BUY_BY_EMAIL % dict(familyName='Upgrade'),
        )),
    ],
    'Upgrade Waterfall': [ 
        ('Upgrade-Regular', dict(
        )),
    ],

    # === PowerLift Try === 
    'PowerLift': [
        ('PowerLift_Try-Tight', dict(
            sample='PowerLift',
        )),
        ('PowerLift_Try-Tight_Outline', dict(
            sample='Outline',
            download='downloads/TYPETR-PowerLift_Try.zip',
            adobe='https://fonts.adobe.com/fonts/powerlift',
            typenetwork='https://store.typenetwork.com/foundry/typetr/fonts/powerlift',
            #google='https://www.google.com/search?q=typetr+powerlift+usage&oq=typetr+powerlift+usage',
            buybyemail=BUY_BY_EMAIL % dict(familyName='PowerLift'),

        )),
        ('PowerLift_Try-Tight_Circle36', dict(
            sample='Circle',
            download='downloads/TYPEYR-PowerLift_Try.zip',
        )),
        ('PowerLift_Try-Tight_Slab24', dict(
            sample='Slab',
            download='downloads/TYPETR-PowerLift_Try.zip',
        )),
    ],

    # === Bitcount Outline Try === 
    'Bitcount Outline Round': [
        ('Bitcount_Try_Mono_Double_Outline-Book_Round', dict(
            sample='Bitcount Book Round',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Round', dict(
            sample='Bitcount Regular Round',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Medium_Round', dict(
            sample='Bitcount Medium Round',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Bold_Round', dict(
            sample='Bitcount Bold Round',
        )),
        ('Bitcount_Try_Mono_Double_Outline-ExtraBold_Round', dict(
            sample='Bitcount XBold Round',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Black_Round', dict(
            sample='Bitcount Black Round',
            download='downloads/TYPETR-Bitcount_Try_Outline-Round.zip',
            seeAlso='https://bitcount.typenetwork.com',
            typenetwork='https://store.typenetwork.com/foundry/typetr/fonts/bitcount',
            buybyemail=BUY_BY_EMAIL % dict(familyName='Bitcount Outline Round'),
        )),
    ],

    # === Bitcount Outline Square Try === 
    'Bitcount Outline Square': [
        ('Bitcount_Try_Mono_Double_Outline-Book_Square', dict(
            sample='Bitcount Book Square',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Square', dict(
            sample='Bitcount Regular Square',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Medium_Square', dict(
            sample='Bitcount Medium Square',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Bold_Square', dict(
            sample='Bitcount Bold Square',
        )),
        ('Bitcount_Try_Mono_Double_Outline-ExtraBold_Square', dict(
            sample='Bitcount XBold Square',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Black_Square', dict(
            sample='Bitcount Black Square',
            download='downloads/TYPETR-Bitcount_Try_Outline-Square.zip',
            seeAlso='https://bitcount.typenetwork.com',
            typenetwork='https://store.typenetwork.com/foundry/typetr/fonts/bitcount',
            buybyemail=BUY_BY_EMAIL % dict(familyName='Bitcount Outline Square'),
        )),
    ],

    # === Bitcount Outline Square Italic Try === 
    'Bitcount Outline Square Italic': [
        ('Bitcount_Try_Mono_Double_Outline-Book_Square_Italic', dict(
            sample='Bitcount Book Sq.Italic',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Square_Italic', dict(
            sample='Bitcount Regular Sq.Italic',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Medium_Square_Italic', dict(
            sample='Bitcount Medium Sq.Italic',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Bold_Square_Italic', dict(
            sample='Bitcount Bold Sq.Italic',
        )),
        ('Bitcount_Try_Mono_Double_Outline-ExtraBold_Square_Italic', dict(
            sample='Bitcount XBold Sq.Italic',
        )),
        ('Bitcount_Try_Mono_Double_Outline-Black_Square_Italic', dict(
            sample='Bitcount Black Sq.Italic',
            download='downloads/TYPETR-Bitcount_Try_Outline-Square_Italic.zip',
            seeAlso='https://bitcount.typenetwork.com',
            typenetwork='https://store.typenetwork.com/foundry/typetr/fonts/bitcount',
            buybyemail=BUY_BY_EMAIL % dict(familyName='Bitcount Outline Square Italic'),
        )),
    ],

    # === Stickway Try === 
    'Stickway': [
        ('Stickway_Try-Thin', dict(
            sample='Stickway Thin',
        )),
        ('Stickway_Try-Regular', dict(
            sample='Stickway Regular',
        )),
        ('Stickway_Try-Bold', dict(
            sample='Stickway Bold',
        )),
        ('Stickway_Try-Black', dict(
            sample='Stickway Black',
            download='downloads/TYPETR-Stickway_Try_BaseMasters.zip',
            #variablefont='downloads/TYPETR-Stickway_Try_VF.zip',
            buybyemail=BUY_BY_EMAIL % dict(familyName='Stickway'),
        )),
    ],

    # === Opcode === 
    'Opcode': [
        ('Opcode_Try-Regular', dict(
            sample='Opcode Regular',
            download='downloads/TYPETR-Opcode_Try_BaseMasters.zip',
            #variablefont='downloads/TYPETR-Opcode_Try_VF.zip',
            buybyemail=BUY_BY_EMAIL % dict(familyName='Opcode'),
        )),
    ],

    # === Responder P === 
    'Responder P': [
        ('Responder_P_Try-Hairline', dict(
            sample='Responder Hairline',
        )),
        ('Responder_P_Try-Regular', dict(
            sample='Responder Regular',
        )),
        ('Responder_P_Try-Black', dict(
            sample='Responder Bold',
        )),
        ('Responder_P_Try-Black', dict(
            sample='Responder Black',
            download='downloads/TYPETR-Responder_P_Try_BaseMasters.zip',
            #variablefont='downloads/TYPETR-Responder_P_Try_VF.zip',
            buybyemail=BUY_BY_EMAIL % dict(familyName='Responder P'),
        )),
    ],

    # === Presti === 
    'Presti': [
        ('Presti_Try-Hairline', dict(
            sample='Presti Hairline',
        )),
        ('Presti_Try-Light', dict(
            sample='Presti Light',
        )),
        ('Presti_Try-Semibold', dict(
            sample='Presti Semibold',
        )),
        ('Presti_Try-Black', dict(
            sample='Presti Black',
        )),
        ('Presti_Try-UltraBlack', dict(
            sample='Presti UltraBlack',
            download='downloads/TYPETR-Presti_Try_BaseMasters.zip',
            #variablefont='downloads/TYPETR-Presti_Try_VF.zip',
            buybyemail=BUY_BY_EMAIL % dict(familyName='Presti'),
        )),
    ],

    # === Promise === 
    'Promise': [
        ('Promise_Try-Medium', dict(
            sample='Presti Medium',
        )),
        ('Promise_Try-Medium_Italic', dict(
            sample='Promise Medium Italic)',
        )),
        ('Promise_Try-Bold', dict(
            sample='Promise Bold',
        )),
        ('Promise_Try-Bold_Italic', dict(
            sample='Promise Bold Italic',
            download='downloads/TYPETR-Promise_Try_BaseMasters001.zip',
            #variablefont='downloads/TYPETR-Promise_Try_VF.zip',
            buybyemail=BUY_BY_EMAIL % dict(familyName='Promise'),
        )),
    ],

    # === Prominence === 
    'Prominence': [
        ('Prominence_Try-ExtraLight', dict(
            sample='Presti Extra Light',
        )),
        ('Prominence_Try-ExtraLight_Italic', dict(
            sample='Presti Extra Light Italic',
        )),
        ('Prominence_Try-Regular', dict(
            sample='Prominence Regular',
        )),
        ('Prominence_Try-Regular_Italic', dict(
            sample='Prominence Italic',
        )),
        ('Prominence_Try-Semibold', dict(
            sample='Prominence Semibold',
        )),
        ('Prominence_Try-Semibold_Italic', dict(
            sample='Prominence Semibold Italic',
        )),
        ('Prominence_Try-Bold', dict(
            sample='Prominence Bold',
        )),
        ('Prominence_Try-Bold_Italic', dict(
            sample='Prominence Bold Italic',
        )),
        ('Prominence_Try-ExtraBold', dict(
            sample='Prominence Extra Bold',
        )),
        ('Prominence_Try-ExtraBold_Italic', dict(
            sample='Prominence Extra Bold Italic',
        )),
        ('Prominence_Try-Black', dict(
            sample='Prominence Black',
        )),
        ('Prominence_Try-Black_Italic', dict(
            sample='Prominence Black Italic',
            download='downloads/TYPETR-Prominence_Try_BaseMasters.zip',
            #variablefont='downloads/TYPETR-Prominence_Try_VF.zip',
            buybyemail=BUY_BY_EMAIL % dict(familyName='Prominence'),
        )),
    ],

}

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
        'fonts/trywebfonts.css', 
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
