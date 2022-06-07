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

class PepperTomTheme(IntoTheWoods):

    logo1 = color(1)
    logo2 = color(0xFF00C1) # Magenta bar of logo
    logo3 = color(0xEC472C) # Orange bar of logo

theme = PepperTomTheme()

siteData = sd = SiteData(id='peppertom', title='Pepper+Tom', theme=theme)
sd.menuName = 'Menu'
sd.year = now().year
sd.copyright = ' | '.join((
    '<a href="https://peppertom.com" target="external">Pepper+Tom</a>',
    '<a href="https://typetr.typenetwork.com">TYPETR</a>',
    '<a href="https://designdesign.space">DesignDesign.Space</a>'))
sd.fontFamily = 'Upgrade'
sd.logo = """<span style="color:#%s;">|</span><span style="color:#%s">d</span><span style="color: #%s;">|</span>""" % (theme.logo2.hex, theme.logo1.hex, theme.logo3.hex)

sd.fontsCss = True
sd.fontFamily = 'Upgrade'
sd.headFont = sd.fontFamily + '-Regular'
sd.bodyFont = sd.fontFamily + '-Book'
sd.logoFontFamily = 'PepperTom'
sd.monoFontFamily = 'Courier New'
sd.iconFontFamily = 'FontAwesome'

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
t1 = 'Pepper+Tom pop-up!'
t2 = 'P+T invites you!'

dk1 = 'Last pieces from several editions of small series. Skirts, pants and scarves for high end stores, are waiting for you.'
dk2 = 'I would love to bring all these beautiful handmade or semi- couture garments into the world for attractive prices :)'
dk3 = 'Call +31 6 41 367 689 or <a href="mailto:claudia@petr.com?subject=Studio visit">email</a> me for an appointment in my studio in Delft. Come by yourself or with maximum two others. '
dk4 = 'The skirts and pants are all different, every piece is unique. there’s a variety of sizes from XXS to XL. Which one will be yours?!'
dk5 = 'The scarves will always fit. Either as a gift for yourself or for someone else.'
dk6 = 'Looking forward seeing you!'

st1 = 'Clear out from several editions of small series'
st2 = 'Together we will make an attractive price'
st3 = 'Call or email for an appointment in the studio'
st4 = 'Every piece is unique'
st5 = 'The scarves will always fit'
st6 = dk6

pqImage = 'images/scarfs/scarf3.png'
pqSubhead = 'Get in touch'
pqHead = 'Call +31 6 41 367 689 or <a href="mailto:claudia@petr.com?subject=Studio visit">email</a> me'

articleInvitation = '%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n' % (dk1, dk2, dk3, dk4, dk5, dk6)

articleFashion = """Where do clothing and fabrics come from? Who made them and under what circumstances? Often there is no answer to these questions, even when asking them in expensive stores. 

Wouldn’t it be nice to wear clothes where it is clear who made them? Where the conditions of fabrication are good and the trade is fair? 

Pepper+Tom wants that sharing experience, collaborating with partners in the clothing chain who think and act the same way. To make the production, resources and materials traceable for every garment. Pepper+Tom supports the idea of ‘true cost’ and ‘slow fashion’, adding to the pleasure of wearing the clothes.
"""

articleScarves = """The scarves are the result of many peoples’ work and creativity from rural Bangladesh to the cities of the Netherlands and the shores of the United States. 

Beautiful women of Bangladesh embroider the scarves by using the traditional Nakshi Kantha technique. The silk of the scarves is made of the best quality, Rajshahi Silk. The fabric is embossed in a workplace in Dhaka and embroidered in Dinajpur, a poor region in the northwest of Bangladesh. 

All under supervision of Kumudini Welfare Trust of Bengal. This NGO is part of the World Fair Trade Forum and Ecota Fair Trade Forum. In 2008 they received the Award of Excellence for Handicrafts South Asia from Unesco. 

Under the name of Generous Gesture, the scarves have won a Bronze Award for the European Design Award 2010 in the category ‘Self Initiated Projects’ 

Generous Gesture has been nominated for the German Design Award 2012. 

Generous Gesture is a people project. Every piece we make is 100% fair trade. The principle of Generous Gesture is creating fair trade with sustainable products. Through an exchange of ideas and skills we create a win-win situation for all concerned parties. 
"""

articleSkirts = """Pepper+Tom skirts are perfect basic items that should not be missing in your wardrobe. They are designed in various sizes, fabrics (cotton, silk and wool) different lengths and delicately fınished with a colored zipper. The skirts are made from sustainable fabrics. Semi couture by a Dutch Atelier. 

Confıdent women accentuate their individuality with their outfıt. Tough boots under a fashionable skirt. High heels under a loose dress or pants. They combine stylish and tough. They choose for comfort above catwalk, appreciating beautiful and well-made garments. They opt for Pepper+Tom. 

Quote’s by Pepper+Tom customers: ‘It’s a simple style, good model, clear!’ ‘I can wear it all day, all night, everywhere’ ‘Very flattering to many fıgure types’ 

Pepper+Tom would like to say to all women: ‘Just keep dancing!’ 

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
sd.bannerSlideShowHeadSizeColor = sd.theme.getColor('lowest', a=0.85)
sd.bannerSlideShowHeadBackgroundColor = 'inherit'
sd.bannerSlideShowHeadShadow = shadow
sd.bannerSlideShowHeadPadding = '1rem'

sd.bannerSlideShowSubheadFont = sd.fontFamily + '-Medium' 
sd.bannerSlideShowSubheadSize = '1.5rem' # Set to siteData
sd.bannerSlideShowSubheadColor = sd.theme.getColor('lowest', a=0.85)

sd.bannerSlideShowSubheadBackgroundColor = 'inherit' #color(0xEC472C, a=0.35).css # sd.theme.getColor('highest', a=0.35)
sd.bannerSlideShowSubheadShadow = shadow
sd.bannerSlideShowSubheadPadding = '1rem'

p.bannerImage_1 = 'images/claar/IMG_7187-1.jpg'
p.bannerTitle_1 = t1
p.bannerSubtitle_1 = st1

p.bannerImage_2 = 'images/claar/IMG_6857.jpeg'
p.bannerTitle_2 = t1
p.bannerSubtitle_2 = st3

p.bannerImage_3 = 'images/claar/IMG_3295.jpeg'
p.bannerTitle_3 = t2
p.bannerSubtitle_3 = st2

p.bannerImage_4 = 'images/claar/IMG_6978.jpeg'
p.bannerTitle_4 = t2
p.bannerSubtitle_4 = st4

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

p.articleImage_1 = ('images/claar/IMG_7187-1.jpg', 'center top')
p.articleSubhead_1 = 'Pepper+Tom pop-up! '
p.articleHead_1 = 'Pepper+Tom is inviting you!'
p.articleText_1 = articleInvitation

# Page index, article 2

p.articleImage_2 = 'images/skirts/img_9595.jpeg'
p.articleSubhead_2 = 'Cool clothes. Designed&nbsp;styles.'
p.articleHead_2 = 'Desirable fabrics & fashion'
p.articleText_2 = articleFashion
p.articleFooter_2 = dk2

# Page index, article 2

p.articleImage_3 = 'images/scarfs/scarf_silver_02.jpg'
p.articleSubhead_3 = 'Sustainable materials. Fair&nbsp;trade.'
p.articleHead_3 = 'Scarves'
p.articleText_3 = articleScarves
p.articleFooter_3 = dk3

# Page index, article 3

p.articleImage_4 = 'images/skirts/rok_lang_geelgroen_08.jpg'
p.articleSubhead_4 = 'Slow fashion.'
p.articleHead_4 = 'Skirts'
p.articleText_4 = articleFashion
p.articleFooter_4 = dk4

# Page index, article 4

p.articleImage_5 = 'images/pants/img_7254.jpeg'
p.articleSubhead_5 = 'Pepper+Tom makes it work.'
p.articleHead_5 = 'Pants'
p.articleText_5 = articlePants
p.articleFooter_5 = dk5

# Page index, slideShow

p.slideShow = True # Turn it on
p.slideShowTitle = 'Lookbook'
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
    ('images/lookbook1/img_7141.jpg', None, 'Love the contrast, love the matching | Menemsha MV'),
    ('images/lookbook1/img_2458.jpg', None, 'Playing with card board, marker and crayons'),
    ('images/lookbook1/img_2361.jpg', None, 'Leafs and light'),
    ('images/lookbook1/claudia_schaduw.jpg', None, 'Thank you sunlight!'),
    ('images/lookbook1/img_86291.jpg', None, 'Sure?!'),
    ('images/lookbook1/img_8857+2.jpg', None, 'Beach fun, no lifeguards around... | MV'),
    ('images/lookbook1/img_8601.jpg', None, 'Impressed by Ursula von Rydingsvard and Alexander Calder at Storm King | NYC'),
    ('images/lookbook1/img_8437.jpg', None, 'Design thru light'),
    ('images/lookbook1/img_8370.jpg', None, 'Inspired by light, reflection, color | Robert Irwin | DIA Beacon NY'),
    ('images/lookbook1/img_8281.jpg', None, 'Reflections'),
    ('images/lookbook1/img_5351.jpg', None, 'Ice design'),
    ('images/lookbook1/img_8575.jpg', None, 'Calder meets the Hudson Valley | Alexander Calder | Storm King NYC'),
    ('images/lookbook1/img_8102.jpg', None, 'Lift your head once in a while, you will love it!'),
    ('images/lookbook1/img_1578.jpg', None, 'Cutting paper letters'),
    ('images/lookbook1/img_7719.jpg', None, 'Color and character'),
    ('images/lookbook1/img_3338.jpg', None, 'Generous Gesture | Embroidered Nakshi Kantha | Detail Latin and Bengali type'),
    ('images/lookbook1/img_7942.jpg', None, 'Doubled'),
    ('images/lookbook1/img_7933.jpg', None, 'Old meets new | Ceiling Cooper Hewitt Museum | NYC'),
    ('images/lookbook1/img_7862.jpg', None, 'Grey tones'),
    ('images/lookbook1/rok_tas_strand_02.jpg', None, 'A repoussoir for Pepper+Tom | MV US'),
    ('images/lookbook1/img_7859.jpg', None, 'Black and white, so strong together'),
    ('images/lookbook1/img_7768.jpg', None, 'So beautiful to get older'),
    ('images/lookbook1/claudia_schaduw_02.jpg', None, 'Pepper+Tom skirt having fun at home'),
    ('images/lookbook1/img_7887.jpg', None, 'Reused fabric | Cooper Hewitt Museum | NYC'),
    ('images/lookbook1/img_7737.jpg', None, 'Above your head in ABC CARPET & HOME | NYC'),
    ('images/lookbook1/img_7645.jpg', None, 'Behind the physical object'),
    ('images/lookbook1/img_6090.jpg', None, 'Rusted TYPETR Promise type in ’s Hertogenbosch | NL'),
    ('images/lookbook1/img_0861.jpg', None, 'Friendly Guy in the City'),
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
    ('images/lookbook1/img_0860.jpg', None, 'Grand Old Lady, an Archetype in the City.'),
    ('images/lookbook1/img_9074.jpg', None, 'Edward Hopper, Hero of light, color, desolation.'),
    ('images/lookbook1/img_9071.jpg', None, 'Scarlet runner beans’ color palet.'),
    ('images/lookbook1/img_9069.jpg', None, 'Charlotte Brontë, more than a wonderful writer.'),
    ('images/lookbook1/rok_tas_strand.jpg', None, 'Skirt reaching the beach, always so good to be there | MV US'),
    ('images/lookbook1/img_9064.jpg', None, 'Surface, light, reflection.'),
    ('images/lookbook1/img_9066.jpg', None, 'Weathered skin.'),
    ('images/lookbook1/img_9075.jpg', None, 'Results of planting, nurturing, harvesting. Mannequins at the Agricultural Fair | MV US'),
    ('images/lookbook1/img_9067.jpg', None, 'Russel Wright’s joy of interior experiments at Manitoga | Garrison NYC'),
    ('images/lookbook1/img_9062.jpg', None, 'Tactility of Richard Serra’s corten steel bodies.'),
    ('images/lookbook1/img_9059.jpg', None, 'Sketchbook | Claudia Mens'),
    ('images/lookbook1/img_9060.jpg', None, 'Spring in Vermont | US'),
    ('images/lookbook1/img_9081.jpg', None, 'Still life at Putney School | Vermont US'),
    ('images/lookbook1/img_9061.jpg', None, 'Passing a garbage bin.'),
    ('images/lookbook1/img_9079.jpg', None, 'Zinnias, the Summer Souls.'),
    ('images/lookbook1/img_9076.jpg', None, 'Coop creations.'),
    ('images/lookbook1/img_9068.jpg', None, 'Wall detail at the Russel Wright Foundation, pine needles and concrete | Garrison NYC'),
    ('images/lookbook1/img_9065.jpg', None, 'Sol LeWitt, achromatic scheme | DIA Beacon NY'),
    ('images/lookbook1/img_3327.jpg', None, 'Generous Gesture | Who’s the Dandy? | Embroidered Nakshi Kantha'),
    ('images/lookbook1/img_9060.jpg', None, 'Fall in the dunes | Wassenaar NL'),
    ('images/lookbook1/rok_tas_bos.jpg', None, 'Skirt on her way to the beach | Martha’s Vineyard US'),
    ('images/lookbook1/img_3336.jpg', None, 'Embroidered type | Generous Gesture'),
    ('images/lookbook1/img_0966.jpg', None, 'Hanging in the balance | Alexander Calder | Witney Museum | NYC'),
    ('images/lookbook1/img_0858.jpg', None, 'Knitting Madison Square by Daniella on Design | NYC'),
    ('images/lookbook1/img_5140.jpg', None, 'Shop window in Antwerp | Belgium'),
    ('images/lookbook1/img_7798.jpg', None, 'Cut out paper, the background appears'),
    ('images/lookbook1/img_7038.jpg', None, 'Layers, always intriguing | Edgartown MV'),
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
p = sd.newPage(id='more-about-scarves', title='More about scarves', template='article')

# Options in generic templates
#   {{articlePageHeader}}
#   {{article1}}
#   {{pullQuote2}}
#   {{article2}}
#   {{pullQuote3}}
#   {{article3}}
#   {{gallery}}

p.articlePageHeader = True # Make the call to website._articlePageHeader(siteData, pageData) available.
p.articlePageHeaderSubhead = 'Kumudini Welfare Trust'
p.articlePageHeaderTitle = 'Women of Bangladesh'

p.article = True 
p.articleSubhead = 'Fruitful collaboration'
p.articleHead = 'More about scarves '
p.articleText = """The shawl is a gift. By giving it, the giver wants to tell something to someone, “I give this unique shawl to my...”. For the receiver it is a way of expression. Depending on how the shawl is folded, emphasis is on either the alliterating typography or the decorative leaves. A new image every time as personal gift. To someone. Or to yourself. The scarves are hand made in a limited edition.

Scarf: ‘Wonderful Woman’, ‘Lovely Lover’, ‘Marvelous Mother’ and ‘Fabulous Friend’ 

<img width="100%" src="images/scarfs/orange_big.jpg">

The scarves of Generous Gesture are always a gift; either to yourself or to someone else. A vibrant combination of color, ornaments and/or typography, they can be worn in many different ways.The shawls are produced in block-print, provided with an embroidered frame, the material is silk,  or a combination of silk and eco cotton. The shawls are made of Rajshahi Bengali silk, woven by the shot or changeant technique. If the fabric moves the color changes and is continuously different. The clarity of the colors is extraordinary! 

<iframe width="100%" height="300px" src="https://www.youtube.com/embed/jSs3vJGHpRE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Scarf ’Gentle Gent’  These scarves are embroidered by hand. Double layered fabrics of silk and cotton. They measure 12 x 65 inch (30 x165 cm). The silver colored silk is made of the best Rajshahi Bengali silk. The off-white cotton is eco friendly produced. 

The scarf says ‘Gentle Gent’ in Latin (English) and in Bengali. Jo de Baerdemaker a typedesigner from Belgium was very helpful with the Bengali type. Visit <a href="http://www.typojo.com" target="external">www.typojo.com</a> to learn more about his work. 

<img width="100%" src="images/scarfs/scarf-silver-03.jpg">

## Wash instructions
<p>Handle with love and care. Wash gently by hand in hand-warm water with detergent for silk. Ironing. Do not bleach, no tumble-dry.</p>

"""

p.pullQuote = True # Trigger the template method
p.pullQuoteImage = pqImage
p.pullQuoteSubhead = pqSubhead
p.pullQuoteHead = pqHead 

p.article_1 = False 
p.pullQuote_1 = False
p.article_2 = False
p.pullQuote_2 = False
p.gallery = False # Ignore the template._gallery method call


#----------------------------------------------------------------------------- 
p = sd.newPage(id='more-about-skirts', title='More about skirts', template='article')

# Options in generic templates
#   {{articlePageHeader}}
#   {{article1}}
#   {{pullQuote2}}
#   {{article2}}
#   {{pullQuote3}}
#   {{article3}}
#   {{gallery}}

p.articlePageHeader = True # Make the call to website._articlePageHeader(siteData, pageData) available.
p.articlePageHeaderSubhead = 'Slow fashion'
p.articlePageHeaderTitle = 'To all women: “Just keep dancing!”'

p.article = True 
p.articleSubhead = 'Supply chain collaboration'
p.articleHead = 'Fabrics of the skirts'
p.articleText = """Capsicum natuurstoffen is a Dutch initiative that uses eco cotton, handwoven in Kerala, India. This handwoven fabric contains small inconsistencies, a characteristic of the handcrafted process. Capsicum has developed an environmentally friendly production process, they encourage their producers to improve working conditions and strive to pay their workers a fair wage. 

In addition to the cottons, Capsicum promotes handwoven silk from Bangkok, Thailand, cooperating with a family business for over 30 years. 

![](images/skirts/IMG_0347-1.jpg)

Zippers are sourced from Italian brand Lampo, certifıed by Oeko-Tex Standard 100.

Pepper+Tom source their eco cotton and ink from Ecological Textiles for their hand painted skirts. This fırm offers a wide range in fabrics, yarns and dyes that are manufactured and processed in a sustainable way. Ecological Textiles stands for environmentally sound production, fair trade and top quality. 

<img width="100%" src="images/skirts/IMG_1328-min.jpg">

From threads to fabrics, from moulding to materials our products comply with all European environmental, occupational safety laws and respect for the workers. 

## Wash instructions 
Eco cotton Machine wash 40°C, ironing, do not bleach, no tumble-dry. Handle with love and care. 

Silk Wash gently only by hand, ironing, do not bleach, no tumble- dry. Handle with love and care. 
"""

p.pullQuote = True # Trigger the template method
p.pullQuoteImage = pqImage
p.pullQuoteSubhead = pqSubhead
p.pullQuoteHead = pqHead 

p.article_1 = False 

p.pullQuote_1 = True # Trigger the template method
p.pullQuoteImage = pqImage
p.pullQuoteSubhead = pqSubhead
p.pullQuoteHead = pqHead 

p.article_2 = False
p.pullQuote_2 = False
p.gallery = False # Ignore the template._gallery method call
   
#----------------------------------------------------------------------------- 
p = sd.newPage(id='more-about-studio', title='More about studio + me', template='article')

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
p.articleSubhead = 'Joy together'
p.articleHead = 'Focus groups'
p.articleText = """

Pepper+Tom feels privileged to work with a dedicated group of women. They give feedback, valuable information about what women want. We believe this is the best way to improve the design of the skirts. “The brand is not a product, it’s the relationship that you build with your customer. The product is just the start, a conversational piece.” Buy less, choose well.

<img width="100%" src="images/focus/damesphotosa3delft2-21x42.jpg">
<img width="100%" src="images/focus/damesphotosa3delft1-21x42.jpg">
<img width="100%" src="images/focus/damesphotosa3-21x42.jpg">
---
## Studio + partners
Pepper+Tom would never exist without a team of dedicated people:

Petr van Blokland *Typedesigner* 

Kirsten Langmuur *Graphic designer* 

Liesbeth Oltmans *Consultant*

Djoeke Delnooz, Claar van Liemt (+ Lucy dog : ) *Models* 

Libby Ellis (Tom) *Creative director* 

Sep Schaffers *Text writer* 

Petra Dijkgraaf *Tailor*

Suzanne Liem *Photographer* 

Pendleton, Boweevil, Capsicum, Ecological Textiles and Bottger *Fabric suppliers*

Claudia Mens (Pepper) *Designer, founder Pepper+Tom*

Pepper+Tom is initiated by Claudia Mens, located at Rietveld 56, 2611 LM in Delft, The Netherlands.
---
## About me

<img width="100%" src="images/contact/image-asset66.jpeg">

“I am the child of the woods. We lived in a wooden house, at a dirt road. Endlessly tinkering with acorns. Myself hiding under the ferns. Preferably in a sweater and pants. Wow, what a freedom, what a space. Always together with other kids.”

“Watching is a verb,” my mother would say “look at the world. Look how beautiful that portrait has been painted.” I drew notebooks. Making atmospheres and environments, little peepshows. Then crept behind my mom’s Husqvarna sewing machine and sewed a wide comfy skirt. To climb into trees. 

After three decades, running a studio from 1980 till 2010, it was time for something else. Claudia went looking and longing for the woods of her childhood. She found that feeling back on Martha's Vineyard in the USA, where she began drawing with childlike pleasure and painting. Arose leafs and fern motifs, inspired by her travels in Africa, South America and Asia. 

She designed a series of scarves with type and motifs of leafs, produced by NGO Kumudini Welfare Trust in Bangladesh. In 2016, she started with a lot of spirit and fun Pepper+Tom. 

Besides the products of Pepper+Tom, similar to work in all of the photo's on this website, design can be made by Claudia as a special custom assignment. Ask her: <a href="mailto:claudia@petr.com?subject=Contact Pepper+Tom">claudia@petr.com</a> 

<img width="100%" src="images/contact/peppertom.png">

## Looking forward seeing you... 

Claudia Mens | claudia@petr.com 

mobile +31 6 41 367 689 | studio +31 15 887 1233 

Rietveld 56 | 2611 LM Delft | The Netherlands 

The company is registered in the Chamber of Commerce (Handelsregister Kamer van Koophandel), by name Buro Petr van Blokland + Claudia Mens, number 27237753 Delft. 

If you have a question not answered in this website, you can send an email (<a href="mailto:claudia@petr.com?subject=Contact Pepper+Tom">claudia@petr.com</a>) and we will respond to you as soon as we can. 

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

