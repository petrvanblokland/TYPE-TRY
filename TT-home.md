~~~
doc.title = 'TYPE TRY'

# Uncomment to see cssId/cssClass markers in the page
#doc.view.showIdClass = True

# Page (Home)
#	Wrapper
#		Header 
#			Logo (+BurgerButton)
#			Navigation/TopMenu/MenuItem(s)
#      Content
#  			Banner
#  			SlideShow (on Home)
#      		Slides
#      		SlideSide
#			Section(s)
#				Introduction
#				Main
#				Mains
#					Main
#				Side
#				Sides
#					Side
#		Footer
#
# ----------------------------------------
# index.html
# ----------------------------------------
page.name = 'Home'
page.url = 'index.html'
content = page.select('Content')
box = content.newBanner()
~~~
# Type in the making. Try it now.

~~~
box = content.newCropped()
~~~
![y=top contain noscale](images/IMG_4539.JPG)

# Hi Honey, I’ll buy you a lunch: Fish’n Chips
~~~
box = content.newTypeList(doc.docLib['fontDataList'], fontSize=40, labelFont='Upgrade-Regular', labelFontSize=18)
~~~

~~~
box = content.newIntroduction()
~~~

# TYPE TRY gives an updated overview of running TYPETR projects. Download sample fonts to test in your designs. Use the type, while it is still in the making. Express wishes and suggestions. Find example templates, that show how we would use our typefaces. Copy code snippets to help you implement TYPETR type. 

~~~ 
from pagebot.constants import *
slideshow = content.newSlideShow(h=300, slideW='100%', slideH=300, startIndex=3, autoHeight=True, carousel=2, dynamicHeight=False, transition='slide', easing=CSS_EASE, frameDuration=4, duration=0.7, pauseOnHit=True, randomPlay=False, slidesLeft=True)
box = slideshow.side

~~~
### One typeface family for all scripts

## Compatible and complete.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nunc magna, blandit et venenatis sit amet, congue in sapien. Donec euismod ex in mauris feugiat, quis commodo massa vestibulum. Sed non laoreet tortor.  

# Contact us

~~~
section = content.newSection()
box = section.newMain()
~~~
## Combine the scripts that you need.

Donec vulputate enim ac condimentum aliquam. Donec commodo mattis nisl. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque a diam a dolor vestibulum placerat. Aenean ornare efficitur justo a efficitur. Aliquam accumsan, velit mollis pellentesque accumsan, orci nulla ullamcorper ligula, imperdiet facilisis quam massa a ipsum. Aliquam vitae aliquet odio. Nulla facilisi. Proin pulvinar nisl quis ipsum vehicula pharetra. Praesent ullamcorper in elit sit amet maximus. 

---
# One family to fit all usage.

Donec euismod ex in mauris feugiat, quis commodo massa vestibulum. Sed non laoreet tortor. Etiam malesuada sem et odio laoreet, vel accumsan quam auctor. Quisque porta libero nunc, at pellentesque mauris dictum faucibus. Nam nec luctus dolor, a euismod diam. Cras non luctus libero, vitae pharetra mauris. Mauris iaculis laoreet quam eu ullamcorper. Ut et vehicula neque, eget imperdiet diam. Nulla eget vulputate libero. 

---
## How it works

* Mauris sagittis, dui at tristique elementum, sapien tortor accumsan nisi, et blandit eros magna nec arcu. Nulla pharetra rutrum dictum. 
* Vivamus congue turpis nunc, non vestibulum odio aliquet in. 
* Aliquam ut dapibus metus, quis vehicula nulla. 
* Nullam semper erat vel turpis dictum, eget hendrerit mauris convallis.
* Nam vehicula eu nisi eget sodales. Vestibulum non finibus est. Mauris auctor ex purus, id bibendum justo ullamcorper nec. Phasellus placerat mollis elit, ac luctus sem pretium non. Mauris iaculis scelerisque iaculis.  
* Nunc dignissim lectus tortor, vel finibus nibh lobortis vitae. Nunc sagittis euismod tortor, ut tempor dui volutpat at.

[More about pricing.](pricing.html)

~~~
box = section.newSide()
~~~
### Download the World Font glyph set as PDF

* [Regular](downloads/WorldFontFullGlyphSet-Regular.pdf)
* [Medium](downloads/WorldFontFullGlyphSet-Medium.pdf)
* [Semi-Bold](downloads/WorldFontFullGlyphSet-SemiBold.pdf)
* [Bold](downloads/WorldFontFullGlyphSet-Bold.pdf)

## Licensing

Aliquam accumsan, velit mollis pellentesque accumsan, orci nulla ullamcorper ligula, imperdiet facilisis quam massa a ipsum. Aliquam vitae aliquet odio. Nulla facilisi. Proin pulvinar nisl quis ipsum vehicula pharetra. Praesent ullamcorper in elit sit amet maximus. 

![w=800 y=top](images/WorldFontFullGlyphSet-Bold_1.png)

