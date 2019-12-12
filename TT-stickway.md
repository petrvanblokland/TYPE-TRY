~~~
# ----------------------------------------
# stickway.html
# ----------------------------------------
page = page.next
page.applyTemplate(template)  
page.name = 'Stickway'
page.url = 'stickway.html'

content = page.select('Content')
box = content.newBanner()
~~~
# TYPETR Stickway [TRY](downloads/TYPETR-Stickway_Try.zip)

Try **Stickway** weights and widths. Download the TYPE-TRY font package [here.](downloads/TYPETR-Stickway_Try_BaseMasters.zip)

~~~
# The Stickway fontDataList is defined by the calling application.
box = content.newTypeList(doc.docLib['fontDataList']['Stickway'], fontSize=44, leading=em(1), labelFont='Upgrade-Regular', labelFontSize=18)
~~~

~~~
section = content.newSection()
box = section.newMain()
~~~

## Supported features

Phasellus rutrum, quam vitae consequat malesuada, mi urna scelerisque est, tempus pulvinar diam metus ut augue. Nam luctus justo et nunc ornare iaculis. Aliquam sollicitudin rutrum nisl, et dictum sem malesuada non. Donec ut nunc eu nibh rutrum molestie at a nisl. Aenean sit amet nibh sagittis, malesuada nisl a, vehicula libero. Morbi lacinia quam ut enim mattis vulputate. Donec finibus in libero in placerat. Praesent rutrum nunc at ultricies egestas.

~~~
box = section.newInfo()
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

The **Stickway** glyph set includes Latin1, Cyrillic and Greek. 

Note that the TYPE-TRY fonts are for review only. Therefor a limited glyphset is implemented, to get an idea how the fonts work in your design. Refer to the Type Network store for a full license or email TYPETR directly.

~~~
box = section.newSide()
# An image of supported glyphs goes here.
~~~

~~~
section = content.newSection()
box = section.newMain()
"""
(This should work as MarkDown table, but it does not seem to parsing by PageBot)
|Style name|OS/2|H-stem width|Inc|Master|
|----|----:|----:|----:|----:|----|
|Thin|270|22|•|
|Light|300|32|+10||
|Book|390|52|+20||
|Regular|400|72|+30|•|
|Semibold|600|112|+40||
|Bold|700|142|+30|•|
|Black|800|182|+40|•|
"""
~~~
## Supported weights

Weight values are respectively OS/2 and H-stem width.

* Thin (270, 22)
* Light (300, 32)
* Book (390, 52)
* Regular (400, 72)
* Semibold (600, 112)
* Bold (700, 142)
* Black (800, 182)

All weights are available as Roman and Italic.

## Supported widths

* Condensed
* Normal
* Expanded

Suspendisse eleifend, nisi at imperdiet placerat, eros neque pellentesque metus, vitae interdum odio ante et est. Phasellus tempus consequat est, nec suscipit orci aliquam et. Aenean vitae erat et erat congue gravida. Maecenas fermentum pellentesque tellus, id facilisis neque rutrum et. Vestibulum id nunc nunc.

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


