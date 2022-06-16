#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#   P A G E B O T  N A N O
#
#   Copyright (c) 2020+ Buro Petr van Blokland + Claudia Mens
#   www.pagebot.io
#   Licensed under MIT conditions
#
#   Supporting DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------

from pagebotnano_060.templates.sitedata import SiteData
from pagebotnano_060.toolbox.dating import now
from pagebotnano_060.themes import *
from pagebotnano_060.toolbox.color import color

#    BackToTheCity
#    BusinessAsUsual
#    FairyTales
#    FreshAndShiny
#    HappyHolidays
#    IntoTheWoods
#    SeasoningTheDish
#    SomethingInTheAir
#    WordlyWise

TRACKING = '0.025rem'
TRACKING_WIDE = '0.1rem'

class TypeTryTheme(IntoTheWoods):

    logo1 = color(1)
    logo2 = color(0xFF00C1) # Magenta bar of logo
    logo3 = color(0xEC472C) # Orange bar of logo

theme = TypeTryTheme()

siteData = sd = SiteData(id='TYPE-TRY', title='TYPE-TRY', theme=theme)
sd.menuName = 'Menu'
sd.year = now().year
sd.copyright = ' | '.join((
    '<a href="https://type-try.com" target="external">TYPE-TRY</a>',
    '<a href="https://typetr.typenetwork.com">TYPETR</a>',
    '<a href="https://designdesign.space">DesignDesign.Space</a>'))
sd.fontFamily = 'Upgrade'
sd.logo = """<img src="images/logos/type-try-logo.gif" width="40%"/>"""

sd.fontsCss = False
sd.fontFamily = 'Upgrade'
sd.headFont = sd.fontFamily + '-Regular'
sd.bodyFont = sd.fontFamily + '-Book'
sd.logoFontFamily = sd.fontFamily + '-Regular'
sd.monoFontFamily = 'Courier New'
sd.iconFontFamily = 'FontAwesome'

sd.headerLogoAlign = 'left'
sd.headerHeight = '4em'

sd.articleHeadPadding = '2em 2em'
sd.articleHeadBorder = '1'
sd.articleHeadBackgroundColor = 'white'
sd.articleHeadOpacity = '0.5'

sd.pTracking = TRACKING
sd.pTrackingWide = TRACKING_WIDE
sd.pLeading = '1.8rem'

sd.footerFont = sd.fontFamily + '-Book_Italic'
sd.footerFontSize = '1em'
sd.footerTracking = TRACKING
sd.footerColor = color(0.5) #sd.theme.getColor('main middle')

sd.menuLinks = True # Force call to template._menuLinks() for all pages.

sd.bodyText2Color = sd.theme.getColor('main text')
sd.bodyText2Size = '1.3rem'
sd.bodyText2Leading = '1.6rem'
sd.bodyText2Font = sd.bodyFont

sd.slideShowBackgroundColor = sd.theme.highest

sd.fonts = (
    'Hairline',
    'Hairline_Italic',
    'Thin',
    'Thin_Italic',
    'Light',
    'Light_Italic',
    'Book',
    'Book_Italic',
    'Regular',
    'Italic',
    'Medium',
    'Medium_Italic',
    'Semibold',
    'Semibold_Italic',
    'Bold',
    'Bold_Italic',
    'Black',
    'Black_Italic',
    'ExtraBlack',
    'ExtraBlack_Italic',
    'UltraBlack',
    'UltraBlack_Italic',
)

# -----------------------------------------------------------------------------
# Page index

p = sd.newPage(id='index', title='Home', template='index')

# Page index, banner
t1 = '' #'TYPE-TRY pop-up!'
t2 = '' #'TYPE-TRY invites you!'

dk1 = 'Try TYPETR fonts for free, with a limited set of characters. Enough to get the idea, and to see how they work in your designs.'
dk2 = 'Not all fonts in this TYPE-TRY website are yet released. Please, check their expected release dates.'
dk3 = 'Call +31 6 41 367 689 or <a href="mailto:claudia@petr.com?subject=Studio visit">email</a> me for an appointment in my studio in Delft. Come by yourself or with maximum two others. '
dk4 = 'The skirts and pants are all different, every piece is unique. there’s a variety of sizes from XXS to XL. Which one will be yours?!'
dk5 = 'The scarves will always fit. Either as a gift for yourself or for someone else.'
dk6 = 'Looking forward seeing you!'

st1 = '' #'Clear out from several editions of small series'
st2 = '' #'Together we will make an attractive price'
st3 = '' #'Call or email for an appointment in the studio'
st4 = '' #'Every piece is unique'
st5 = '' #'The scarves will always fit'
st6 = '' #dk6

pqImage = 'images/scarfs/scarf3.png'
pqSubhead = 'Get in touch'
pqHead = 'Call +31 6 2421 9502 or <a href="mailto:tptr@petr.com?subject=TYPE-TRY typedesign">email</a> me'

articleInvitation = '%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n' % (dk1, dk2, dk3, dk4, dk5, dk6)

articleFashion = """Where do clothing and fabrics come from? Who made them and under what circumstances? Often there is no answer to these questions, even when asking them in expensive stores. 

Wouldn’t it be nice to wear clothes where it is clear who made them? Where the conditions of fabrication are good and the trade is fair? 

TYPE-TRY wants that sharing experience, collaborating with partners in the clothing chain who think and act the same way. To make the production, resources and materials traceable for every garment. TYPE-TRY supports the idea of ‘true cost’ and ‘slow fashion’, adding to the pleasure of wearing the clothes.
"""

articleScarves = """The scarves are the result of many peoples’ work and creativity from rural Bangladesh to the cities of the Netherlands and the shores of the United States. 

Beautiful women of Bangladesh embroider the scarves by using the traditional Nakshi Kantha technique. The silk of the scarves is made of the best quality, Rajshahi Silk. The fabric is embossed in a workplace in Dhaka and embroidered in Dinajpur, a poor region in the northwest of Bangladesh. 

All under supervision of Kumudini Welfare Trust of Bengal. This NGO is part of the World Fair Trade Forum and Ecota Fair Trade Forum. In 2008 they received the Award of Excellence for Handicrafts South Asia from Unesco. 

Under the name of Generous Gesture, the scarves have won a Bronze Award for the European Design Award 2010 in the category ‘Self Initiated Projects’ 

Generous Gesture has been nominated for the German Design Award 2012. 

Generous Gesture is a people project. Every piece we make is 100% fair trade. The principle of Generous Gesture is creating fair trade with sustainable products. Through an exchange of ideas and skills we create a win-win situation for all concerned parties. 
"""

articleSkirts = """TYPE-TRY skirts are perfect basic items that should not be missing in your wardrobe. They are designed in various sizes, fabrics (cotton, silk and wool) different lengths and delicately fınished with a colored zipper. The skirts are made from sustainable fabrics. Semi couture by a Dutch Atelier. 

Confıdent women accentuate their individuality with their outfıt. Tough boots under a fashionable skirt. High heels under a loose dress or pants. They combine stylish and tough. They choose for comfort above catwalk, appreciating beautiful and well-made garments. They opt for TYPE-TRY. 

Quote’s by TYPE-TRY customers: ‘It’s a simple style, good model, clear!’ ‘I can wear it all day, all night, everywhere’ ‘Very flattering to many fıgure types’ 

TYPE-TRY would like to say to all women: ‘Just keep dancing!’ 

All skirts have a A-line. There are three different lengths. Skirts with and without waistbands. Iconic, centerpiece items: Last for ever!
"""

articlePants = """The fabric of these pants has been produced by the best craftsmen of Kumudini Welfare Trust of Bengal. Beautiful women who live in Dinajpur, a poor region in the northwest of Bangladesh, have mastered the traditional embroidery technique Nakshi Kantha. This is a running stitch technique entirely embroidered by hand. The fabrics of the pants are or cotton double layered, or a combination of cotton and silk. The fabrics are natural dyed. Small inconsistencies are characteristics of the handcrafted process. The pants are feminine and cool. You can wear them chic, classic and casual, They will mix and match with your wardrobe for almost every occasion. We hope you will wear them with joy and happiness.

All pants have wide legs, with or without a waistband. All very comfortable to wear. Iconic, centerpiece items:Timeless!

The pants are handmade in a Dutch atelier. 

## Wash instruction 
Handle with love and care, wash gently only hand-wash, ironing, do not bleach, no tumble-dry, chemical cleaning possible (not necessary).
"""

p.bannerSlideShow = True
shadow = '4px 4px 6px rgba(0, 0, 0, 0.65)'
sd.bannerFullHeight = '100vh' # Height of banner
sd.bannerFullHeightMax980 = '90vh' # Height of banner in media
sd.bannerFullHeightMax1280 = '80vh' # Height of banner in media
sd.bannerHalfHeight = '50vh' # Half height of banner
sd.bannerSlideShowHeadFont = sd.fontFamily + '-Medium_Italic' 
sd.bannerSlideShowHeadSize = '5rem' # Set to siteData
sd.bannerSlideShowHeadSizeColor = sd.theme.getColor('main', a=0.85)
sd.bannerSlideShowHeadBackgroundColor = 'white'
sd.bannerSlideShowHeadOpacity = '0.75'
#sd.bannerSlideShowHeadShadow = shadow
sd.bannerSlideShowHeadPadding = '1rem'

sd.bannerSlideShowSubheadFont = sd.fontFamily + '-Medium' 
sd.bannerSlideShowSubheadSize = '1.5rem' # Set to siteData
sd.bannerSlideShowSubheadColor = sd.theme.getColor('lowest', a=0.85)

sd.bannerSlideShowSubheadBackgroundColor = 'inherit' #color(0xEC472C, a=0.35).css # sd.theme.getColor('highest', a=0.35)
sd.bannerSlideShowSubheadShadow = shadow
sd.bannerSlideShowSubheadPadding = '1rem'

# Title slide show
for n, (image, title, subTitle) in enumerate((
    (   'images/booklet/Typetr_Typographics_2022_0930.jpg',
        """[html]<span style="font-family:Presti_Display-Normal;font-size:48;color:red;font-feature-settings:'liga';">T~tlu1~mld2~bld4~brd3r~tru1y~tru1 P~blu3~bld2~brd3~tlu3~tld1r~blu1e~mld1s~tlu5t~bld4i~trd3~brd4</span>""", 
        ''),
    (   'images/booklet/Typetr_Typographics_2022_0928.jpg',
        """[html]<span style="font-family:Responder_P-Black;font-size:48;font-feature-settings:'clig';">Try Responder</span>""",
        ''),
    (   'images/social/Upgrade_in_use_08_Keep_calm.jpg',
        '[html]<span style="font-family:Upgrade-Medium;font-size:48">Try Upgrade</span>', 
        ''),
    (   'images/social/Bitcount_in_use_02.jpg',
        '[html]<span style="font-family:Bitcount_Mono_Outline_Double_Round-ExtraBold;font-size:48">Try Bitcount Outline</span>', 
        ''),
    (   'images/booklet/Typetr_Typographics_2022_0910.jpg',
        '[html]<span style="font-family:PowerLift-Tight;color:red;">Try Powerlift</span>', 
        ''),
    (   'images/booklet/Typetr_Typographics_2022_0924.jpg',
        'Try Proforma Pro, soon...', 
        ''),
    )):
    setattr(p, 'bannerImage_%d' % (n+1), image)
    setattr(p, 'bannerTitle_%d' % (n+1), title)
    setattr(p, 'bannerSubtitle_%d' % (n+1), subTitle)

# Page index, subscriptionForm

p.subscriptionForm = True
p.subscriptionFormHead = 'Yes, I am interested, ...'

# Page index, article 1

p.imagesArticle = True # Trigger the template._imagesArticle call
# CSS
sd.articleHeadSize = '2rem';
sd.articleHeadColor = sd.theme.getColor('accent text')
sd.articleSubheadSize = '1.5rem';
sd.articleSubheadColor = sd.articleHeadColor

# Page index, article invitation

p.articleImage_1 = ('images/booklet/Typetr_Typographics_2022_0914.jpg', 'center top')
p.articleSubhead_1 = 'TYPE-TRY pop-up! '
p.articleHead_1 = 'TYPETR upcoming releases'
p.articleText_1 = articleInvitation

# Page index, article 2

p.articleImage_2 = 'images/typetr/Presti_in_use_02.jpg'
p.articleSubhead_2 = 'Cool clothes. Designed&nbsp;styles.'
p.articleHead_2 = 'Desirable fabrics & fashion'
p.articleText_2 = articleFashion
p.articleFooter_2 = dk2

# Page index, slideShow

p.slideShow = True # Turn it on
p.slideShowTitle = 'TYPETR fonts in use'
# Works for all slide shows in CSS, does not need an item index
sd.slideShowTitleFont = 'Upgrade-Light'
sd.slideShowTitleFontSize = '5rem';
sd.slideShowTitlePadding = '0px 36px 0px 36px'
sd.slideShowTitleColor = sd.theme.white
sd.slideShowTitleTracking = '0rem'
sd.slideShowBackgroundColor = sd.theme.gray.css

p.slideShowHeight = 500
p.slideShowDynamicHeight = False
p.slideShowCarousel = 2 # Number of slides
p.slideShowControls = False
p.slideShowPager = False
p.slideShowTimer = 4
p.slideShowDuration = 0.7
p.slideShowJsCallbackBefore = 'slideShowCaptionUpdate'
p.slideShowCaptionMarginBottom = 80
p.slideShowCaptionFontSize = 32
p.slideShowCaptionFont = 'Upgrade-Book_Italic'
p.slideShowImages = (
    # Name, position (e.g. 'center top'), caption
    ('Typetr_Typographics_2022_098.jpg', None, 'a'),
    ('Typetr_Typographics_2022_099.jpg', None, 'a'),
    ('Typetr_Typographics_2022_0910.jpg', None, 'a'),
    ('Typetr_Typographics_2022_0911.jpg', None, 'a'),
    ('Typetr_Typographics_2022_0912.jpg', None, 'a'),
    ('Typetr_Typographics_2022_0913.jpg', None, 'a'),
    ('Typetr_Typographics_2022_0914.jpg', None, 'a'),
    ('Typetr_Typographics_2022_0915.jpg', None, 'a'),
    ('Typetr_Typographics_2022_0920.jpg', None, 'a'),
    ('Typetr_Typographics_2022_0924.jpg', None, 'a'),
    ('Typetr_Typographics_2022_0925.jpg', None, 'a'),
    ('Typetr_Typographics_2022_0930.jpg', None, 'a'),
    ('Typetr_Typographics_2022_0931.jpg', None, 'a'),
    ('Typetr_Typographics_2022_0928.jpg', None, 'a'),
)

p.slideShow_1 = True # Turn it on
p.slideShowTitle_1 = 'Lookbook'
p.slideShowHeight_1 = 500
p.slideShowDynamicHeight_1 = False
p.slideShowCarousel_1 = 2 # Number of slides
p.slideShowControls_1 = False
p.slideShowPager_1 = False
p.slideShowTimer_1 = 4
p.slideShowDuration_1 = 0.7
p.slideShowJsCallbackBefore_1 = 'slideShowCaptionUpdate_1'
p.slideShowCaptionMarginBottom_1 = 80
p.slideShowCaptionFontSize_1 = 32
p.slideShowCaptionFont_1 = 'Upgrade-Book_Italic'
p.slideShowImages_1 = (
    ('images/booklet/Typetr_Typographics_2022_095.jpg', None, 'A'),
    ('images/booklet/Typetr_Typographics_2022_094.jpg', None, 'B'),
    ('images/booklet/Typetr_Typographics_2022_093.jpg', None, 'C'),
    ('images/booklet/Typetr_Typographics_2022_092.jpg', None, 'D'),
    ('images/booklet/Typetr_Typographics_2022_091.jpg', None, 'E'),
)
# Page index, deck

sd.deckFont = 'Upgrade-Light_Italic'
sd.deckFontSize = '4rem'
sd.deckFontLeading = '1.2em'
sd.deckFontColor = '#FFF' # sd.theme.getColor('main text diap')
sd.deckBackgroundColor = color(0, a=0).css

p.deck = True # Trigger the template method
p.deckImage = 'images/scarfs/scarf3.png'
p.deckHead = dk1

p.deck_1 = True # Trigger the template method
p.deckImage_1 = 'images/scarfs/scarf3.png'
p.deckHead_1 = dk2

# Page index, pullquote

p.pullQuote = True # Trigger the template method
p.pullQuoteImage = pqImage
p.pullQuoteSubhead = pqSubhead
p.pullQuoteHead = pqHead 

p.gallery = False # Trigger the template._gallery method call
'''
p.galleryHead = 'Gallery head'
p.gallerySubhead = 'Gallery subhead'
p.galleryImage_1 = 'images/notes/IMG_0926.jpeg'
p.galleryCaption_1 = """Caption of this image. A very long one. Cras aliquet urna ut sapien tincidunt, quis malesuada elit facilisis. Vestibulum sit amet tortor velit. Nam elementum nibh a libero pharetra elementum."""
p.galleryImage_2 = 'images/notes/IMG_0929.jpeg'
p.galleryCaption_2 = 'Short caption of this image.'  
p.galleryImage_3 = 'images/notes/IMG_0933.jpeg'
p.galleryImage_4 = 'images/notes/IMG_0934.jpeg'
p.galleryImage_5 = 'images/notes/IMG_0935.jpeg'
p.galleryImage_6 = 'images/notes/IMG_0936.jpeg'
'''

#----------------------------------------------------------------------------- 
p = sd.newPage(id='more-about-typetr', title='More about TYPETR foundry', template='article')

# Options in generic templates
#   {{articlePageHeader}}
#   {{article1}}
#   {{pullQuote2}}
#   {{article2}}
#   {{pullQuote3}}
#   {{article3}}
#   {{gallery}}

p.articlePageHeader = True # Make the call to website._articlePageHeader(siteData, pageData) available.
p.articlePageHeaderSubhead = 'People project'
p.articlePageHeaderTitle = 'Studio + me'

p.article = True 
p.articleSubhead = 'Work together'
p.articleHead = 'Focus groups'
p.articleText = """

TYPETR feels privileged to work with a dedicated group of women. They give feedback, valuable information about what women want. We believe this is the best way to improve the design of the skirts. “The brand is not a product, it’s the relationship that you build with your customer. The product is just the start, a conversational piece.” Buy less, choose well.

<img width="100%" src="images/focus/damesphotosa3delft2-21x42.jpg">
<img width="100%" src="images/focus/damesphotosa3delft1-21x42.jpg">
<img width="100%" src="images/focus/damesphotosa3-21x42.jpg">
---
## Foundry + partners
TYPETR would never exist without a team of dedicated people:

Petr van Blokland *Typedesigner* 

Tilmann Hielscher *Typedesigner*

Kirsten Langmuur *Graphic designer* 

Paul Roos *Graphic designer*

TYPETR is initiated by Petr van Blokland, located at Boomsluiterskade 372/367 2511 VH The Hague, The Netherlands.
---
## About me

<img width="100%" src="images/contact/image-asset66.jpeg">

“I am the child of the woods. We lived in a wooden house, at a dirt road. Endlessly tinkering with acorns. Myself hiding under the ferns. Preferably in a sweater and pants. Wow, what a freedom, what a space. Always together with other kids.”

“Watching is a verb,” my mother would say “look at the world. Look how beautiful that portrait has been painted.” I drew notebooks. Making atmospheres and environments, little peepshows. Then crept behind my mom’s Husqvarna sewing machine and sewed a wide comfy skirt. To climb into trees. 

After three decades, running a studio from 1980 till 2010, it was time for something else. Claudia went looking and longing for the woods of her childhood. She found that feeling back on Martha's Vineyard in the USA, where she began drawing with childlike pleasure and painting. Arose leafs and fern motifs, inspired by her travels in Africa, South America and Asia. 

She designed a series of scarves with type and motifs of leafs, produced by NGO Kumudini Welfare Trust in Bangladesh. In 2016, she started with a lot of spirit and fun TYPE-TRY. 

Besides the products of TYPE-TRY, similar to work in all of the photo's on this website, design can be made by Claudia as a special custom assignment. Ask her: <a href="mailto:claudia@petr.com?subject=Contact TYPE-TRY">claudia@petr.com</a> 

<img width="100%" src="images/contact/TYPE-TRY.png">

## Looking forward seeing you... 

Petr van Blokland | tptr@petr.com 

mobile +31 6 2421 9502

Boomsluiterskade 372/367 2511 VH The Hague | The Netherlands 

The company is registered in the Chamber of Commerce (Handelsregister Kamer van Koophandel), by name Buro Petr van Blokland + Claudia Mens, number 27237753 Delft. 

If you have a question not answered in this website, you can send an email (<a href="mailto:claudia@petr.com?subject=Contact TYPE-TRY">claudia@petr.com</a>) and we will respond to you as soon as we can. 

"""

p.pullQuote = True # Trigger the template method
p.pullQuoteImage = pqImage
p.pullQuoteSubhead = pqSubhead
p.pullQuoteHead = pqHead 

p.article_1 = False 
p.pullQuote_1 = False
p.article_2 = False
p.pullQuote_2 = False
p.gallery = False 

