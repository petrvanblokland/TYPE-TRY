~~~
# ----------------------------------------
# Studies/2019-studies.html
# ----------------------------------------
page = page.next
page.applyTemplate(template)  
page.name = 'Prominence'
page.url = 'prominence.html'

content = page.select('Content')
box = content.newBanner()
~~~
# World Font Specifications

~~~ 
from pagebot.constants import *
slideshow = content.newSlideShow(h=300, slideW='100%', slideH=300, startIndex=3, autoHeight=True, carousel=2, dynamicHeight=False, transition='slide', easing=CSS_EASE, frameDuration=4, duration=0.7, pauseOnHit=True, randomPlay=False, slidesLeft=True)
box = slideshow.side

~~~
### Lorem ipsum dolor sit amet

## Donec euismod ex in mauris feugiat.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nunc magna, blandit et venenatis sit amet, congue in sapien. Donec euismod ex in mauris feugiat, quis commodo massa vestibulum. Sed non laoreet tortor.  

# Contact us

~~~
box = slideshow.slides
~~~

~~~
section = content.newSection()
box = section.newMain()
~~~
## Supported scripts

Aliquam at dapibus lacus. Phasellus molestie ante in tempus vehicula. Suspendisse eleifend, nisi at imperdiet placerat, eros neque pellentesque metus, vitae interdum odio ante et est. Phasellus tempus consequat est, nec suscipit orci aliquam et. Aenean vitae erat et erat congue gravida. Maecenas fermentum pellentesque tellus, id facilisis neque rutrum et. Vestibulum id nunc nunc.

![](images/GlyphSets-InPractice.png)

[See more about the support scripts.](scripts.html)

~~~
section = content.newSection()
box = section.newMain()
~~~
## Supported features

Phasellus rutrum, quam vitae consequat malesuada, mi urna scelerisque est, tempus pulvinar diam metus ut augue. Nam luctus justo et nunc ornare iaculis. Aliquam sollicitudin rutrum nisl, et dictum sem malesuada non. Donec ut nunc eu nibh rutrum molestie at a nisl. Aenean sit amet nibh sagittis, malesuada nisl a, vehicula libero. Morbi lacinia quam ut enim mattis vulputate. Donec finibus in libero in placerat. Praesent rutrum nunc at ultricies egestas.

![Features](images/UpgradeFeatures.png)

~~~
box = section.newInfo()
~~~

Phasellus rutrum, quam vitae consequat malesuada, mi urna scelerisque est, tempus pulvinar diam metus ut augue. Nam luctus justo et nunc ornare iaculis. Aliquam sollicitudin rutrum nisl, et dictum sem malesuada non. Donec ut nunc eu nibh rutrum molestie at a nisl. Aenean sit amet nibh sagittis, malesuada nisl a, vehicula libero. Morbi lacinia quam ut enim mattis vulputate. Donec finibus in libero in placerat. Praesent rutrum nunc at ultricies egestas.

![](images/TYPETR-Upgrade-Screen.png)

~~~
section = content.newSection()
box = section.newMain()
~~~
## Supported glyphs

Sed rhoncus pellentesque eros, in commodo sapien suscipit vel. Proin elit felis, pulvinar ac tellus ut, aliquam eleifend libero. Sed id bibendum metus. Pellentesque tincidunt ligula non quam varius, et luctus neque aliquam. Morbi eget cursus orci. Praesent faucibus placerat massa, a condimentum est pretium pulvinar. Maecenas ultricies sapien id ipsum ultrices sollicitudin. 

### Download the World Font glyph set as PDF

* [Regular](downloads/WorldFontFullGlyphSet-Regular.pdf)
* [Medium](downloads/WorldFontFullGlyphSet-Medium.pdf)
* [Semi-Bold](downloads/WorldFontFullGlyphSet-SemiBold.pdf)
* [Bold](downloads/WorldFontFullGlyphSet-Bold.pdf)

~~~
box = section.newSide()
~~~

![Regular](images/WorldFontFullGlyphSet-Regular_1.png)

~~~
section = content.newSection()
box = section.newMain()
~~~
## Supported weights

Suspendisse eleifend, nisi at imperdiet placerat, eros neque pellentesque metus, vitae interdum odio ante et est. Phasellus tempus consequat est, nec suscipit orci aliquam et. Aenean vitae erat et erat congue gravida. Maecenas fermentum pellentesque tellus, id facilisis neque rutrum et. Vestibulum id nunc nunc.

### World Font Sans

![Weights Sans](images/WF-Image40_1.png)

### World Font Slab

![Weights Slab](images/WF-Image30_1.png)

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

![w=800 y=top](images/Upgrade-BoldOutline-FontWindow.png)