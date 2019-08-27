~~~
# ----------------------------------------
# other.html
# ----------------------------------------
page = page.next
page.applyTemplate(template)  
page.name = 'Other'
page.url = 'other.html'

content = page.select('Content')
box = content.newBanner()
~~~
# Other projects

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

[See more about the support scripts.](scripts.html)

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

Sed rhoncus pellentesque eros, in commodo sapien suscipit vel. Proin elit felis, pulvinar ac tellus ut, aliquam eleifend libero. Sed id bibendum metus. Pellentesque tincidunt ligula non quam varius, et luctus neque aliquam. Morbi eget cursus orci. Praesent faucibus placerat massa, a condimentum est pretium pulvinar. Maecenas ultricies sapien id ipsum ultrices sollicitudin. 

### Download the Upgrade CJK glyph set as PDF

~~~
box = section.newSide()
~~~

~~~
section = content.newSection()
box = section.newMain()
~~~
## Supported weights

Suspendisse eleifend, nisi at imperdiet placerat, eros neque pellentesque metus, vitae interdum odio ante et est. Phasellus tempus consequat est, nec suscipit orci aliquam et. Aenean vitae erat et erat congue gravida. Maecenas fermentum pellentesque tellus, id facilisis neque rutrum et. Vestibulum id nunc nunc.

### Upgrade CJK Sans

### Upgrade CJK Slab

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

