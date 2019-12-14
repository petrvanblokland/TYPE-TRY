~~~
# ----------------------------------------
# responder-p.html
# ----------------------------------------
page = page.next
page.applyTemplate(template)  
page.name = 'Responder-P'
page.url = 'responder-p.html'

content = page.select('Content')
box = content.newBanner()
~~~
# <span class="c2sc">TYPETR</span> Responder-P [TRY](downloads/TYPETR-Responder_P_Try_BaseMasters001.zip) it now.

Try the **Responder-P** weights and widths. Download the TYPE-TRY font package [here.](downloads/TYPETR-Responder_Try_BaseMasters001.zip)
~~~
# The Responder-P fontDataList is defined by the calling application.
fonts = doc.docLib['fontDataList']['Responder-P'] # [(fontName, font), ...]
box = content.newTypeList(fonts, fontSize=44, leading=em(1), labelFont='Upgrade-Regular', labelFontSize=18)

section = content.newSection()
box = section.newMain()
~~~
## Supported features

~~~
# fonts is defined above.
# Add intended default tags as long as the font is not complete.
defaultTags = ('locl', 'frac', 'numr', 'dnom', 'sups', 'sinf', 'onum', 'lnum', 'case', 'smcp', 'c2sc', 'tnum', 'pnum', 'liga', 'ss08', 'ss10', 'zero')
defaultTags = None
box.newTypeFeatures(fontDataList=fonts, defaultTags=defaultTags, fontSize=44, leading=em(1), labelFont='Upgrade-Regular', labelFontSize=18)

#box = section.newInfo()
~~~

Phasellus rutrum, quam vitae consequat malesuada, mi urna scelerisque est, tempus pulvinar diam metus ut augue. Nam luctus justo et nunc ornare iaculis. Aliquam sollicitudin rutrum nisl, et dictum sem malesuada non. Donec ut nunc eu nibh rutrum molestie at a nisl. Aenean sit amet nibh sagittis, malesuada nisl a, vehicula libero. Morbi lacinia quam ut enim mattis vulputate. Donec finibus in libero in placerat. Praesent rutrum nunc at ultricies egestas.

~~~
section = content.newSection()
box = section.newMain()
~~~
## Supported glyphs

~~~
# fonts is defined above.
box.newTypeGlyphSet(fonts, fontSize=44, leading=em(1), labelFont='Upgrade-Regular', labelFontSize=18)

#box = section.newInfo()
~~~

The **Responder-P** glyph set includes Latin1, Cyrillic and Greek. 

Note that the TYPE-TRY fonts are for review only. Therefor a limited glyphset is implemented, to get an idea how the fonts work in your design. Refer to the Type Network store for a full license or email TYPETR directly.

~~~
box = section.newSide()
# Side image with supported glyphs here.
~~~

~~~
section = content.newSection()
box = section.newMain()
~~~
## Supported weights

Weight values are respectively OS/2 and H-stem width.

* Hairline (260, 16)
* Thin (270, 22)
* Light (300, 32)
* Book (390, 52)
* Regular (400, 72)
* Semibold (600, 112)
* Bold (700, 142)
* Black (800, 182)

All weights are available as Roman and Italic.

~~~
box = section.newSide()
# Side image with supported glyphs here.
~~~

~~~
section = content.newSection()
box = section.newMain()
~~~
## Supported axes as Variable Font

* wght (16, 90, 256) Weight Hairline:16, Light:32, Regular:90 Bold:150 Black:256
* wdth (70, 100, 130) Width in percentage to Regular
* CATL (0, 0, 500) Catalog of incompatible designs
* opsz (8, 24, 24) Optical size, optimized for small sizes 
* RNDS (0, 0, 48) Maximum size of rounding corners for Regular. Serif roundings are smaller, limited to half of any stem.
* GRAD (-8, 0, 8) Relative grade correction of stems 

### Catalog selectors

* SANS (0-99)  Sans 
* mono (100-199) Sans mono spaced
* SLAB (200-299) Slab serif
* FLRS (300-399)  Sans with expanding flourishes
* LAMP (400-499) Cabaret-like lamps
* SCRP (500-600) Script (italic) with connecting latin glyphs.

~~~
box = section.newSide()
# Side image with supported glyphs here.
~~~

~~~
section = content.newSection()
box = section.newMain()
~~~
## Pricing

Sed rhoncus pellentesque eros, in commodo sapien suscipit vel. Proin elit felis, pulvinar ac tellus ut, aliquam eleifend libero. Sed id bibendum metus. Pellentesque tincidunt ligula non quam varius, et luctus neque aliquam. Morbi eget cursus orci. Praesent faucibus placerat massa, a condimentum est pretium pulvinar. Maecenas ultricies sapien id ipsum ultrices sollicitudin. 

Phasellus rutrum, quam vitae consequat malesuada, mi urna scelerisque est, tempus pulvinar diam metus ut augue. Nam luctus justo et nunc ornare iaculis. Aliquam sollicitudin rutrum nisl, et dictum sem malesuada non. Donec ut nunc eu nibh rutrum molestie at a nisl. Aenean sit amet nibh sagittis, malesuada nisl a, vehicula libero. Morbi lacinia quam ut enim mattis vulputate. Donec finibus in libero in placerat. Praesent rutrum nunc at ultricies egestas.

[See more about pricing here.](pricing.html)

~~~
box = section.newCropped()
~~~


