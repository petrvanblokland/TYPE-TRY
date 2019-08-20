
~~~
# ----------------------------------------
# contact.html
# ----------------------------------------
page = page.next
page.applyTemplate(template)  
page.name = 'Contact'
page.url = 'contact.html'

content = page.select('Content')
box = content.newBanner()
~~~
# Contact us for a free sample 

~~~
from pagebot.constants import *
slideshow = content.newSlideShow(h=300, slideW='100%', slideH=300, startIndex=1, autoHeight=True, carousel=2, dynamicHeight=False, transition='slide', easing=CSS_EASE, frameDuration=4, duration=0.7, pauseOnHit=True, randomPlay=False)
box = slideshow.slides

#![w=200 y=top](images/BK-Graphic-Design.png)
~~~

![w=450 y=top](images/bierCoverPages2-Dutch_1.png)
![w=450 y=top](images/IMG_4826.jpeg)
![w=450 y=top](images/SketchingTypeDesign.png)
![w=450 y=top](images/travelCoverPages_1.png)![w=450 y=top](images/travelCoverPages1x_1.png)

~~~ 
box = slideshow.side
~~~

## What is your type strategy?

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin in nibh eget diam suscipit bibendum eu id quam. Aliquam velit odio, vehicula sed lectus non, vulputate feugiat neque. Ut sit amet consequat ex. Praesent malesuada dui mauris, ac tempus purus luctus rutrum. Nullam posuere mattis urna, eget venenatis neque faucibus ac. Praesent vel pharetra urna. 

# Contact us

~~~
section = content.newSection()
box = section.newMain()
~~~

## Arphic

Nam leo orci, condimentum vel nunc et, euismod varius nisl. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut id imperdiet elit. 

~~~
box = box.newInfo()
~~~

Nulla lacus nibh, dignissim ac quam sit amet, vulputate pulvinar nisl. Mauris viverra finibus interdum. Praesent efficitur arcu id libero vulputate tristique. Suspendisse lectus nisi, bibendum nec mauris at, vestibulum pulvinar sapien. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Suspendisse non libero in ex vestibulum bibendum sed sit amet lectus. Nullam aliquam laoreet fringilla. Phasellus ut diam accumsan, bibendum nisi sed, laoreet sem.

~~~
box = section.newSide()
~~~

* Cras vel leo sed turpis
* Bibendum tempus. 
* Vestibulum vitae porta urna. 
* Nunc pellentesque metus in nunc lobortis, sed finibus massa tincidunt. 
* Ut fringilla condimentum nulla.

~~~
section = content.newSection()
box = section.newMain()
~~~

## Hanyi

Nam leo orci, condimentum vel nunc et, euismod varius nisl. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut id imperdiet elit. Nulla lacus nibh, dignissim ac quam sit amet, vulputate pulvinar nisl. Mauris viverra finibus interdum. 

~~~
box = box.newInfo()
~~~

Praesent efficitur arcu id libero vulputate tristique. Suspendisse lectus nisi, bibendum nec mauris at, vestibulum pulvinar sapien. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Suspendisse non libero in ex vestibulum bibendum sed sit amet lectus. Nullam aliquam laoreet fringilla. Phasellus ut diam accumsan, bibendum nisi sed, laoreet sem.

~~~
box = section.newSide()
~~~

* Cras vel leo sed turpis
* Bibendum tempus. 
* Vestibulum vitae porta urna. 
* Nunc pellentesque metus in nunc lobortis, sed finibus massa tincidunt. 
* Ut fringilla condimentum nulla.

~~~
section = content.newSection()
box = section.newMain()
~~~

## Cadson Demak 

Nam leo orci, condimentum vel nunc et, euismod varius nisl. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut id imperdiet elit. 

~~~
box = box.newInfo()
~~~

Nulla lacus nibh, dignissim ac quam sit amet, vulputate pulvinar nisl. Mauris viverra finibus interdum. Praesent efficitur arcu id libero vulputate tristique. Suspendisse lectus nisi, bibendum nec mauris at, vestibulum pulvinar sapien. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. 

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin in nibh eget diam suscipit bibendum eu id quam. Aliquam velit odio, vehicula sed lectus non, vulputate feugiat neque. Ut sit amet consequat ex. Praesent malesuada dui mauris, ac tempus purus luctus rutrum. Nullam posuere mattis urna, eget venenatis neque faucibus ac. Praesent vel pharetra urna. Quisque pharetra egestas consequat. Curabitur eget elit rutrum, aliquet quam sed, consectetur massa. Vivamus placerat quis ligula nec maximus. Etiam eu mollis nisl. Etiam accumsan sem urna, eu sodales dolor consectetur eget. Mauris porttitor sem metus, non posuere nulla porttitor sit amet. Donec eget augue ut orci scelerisque ullamcorper quis sagittis.

~~~
box = section.newSide()
~~~

* Cras vel leo sed turpis
* Bibendum tempus. 
* Vestibulum vitae porta urna. 
* Nunc pellentesque metus in nunc lobortis, sed finibus massa tincidunt. 
* Ut fringilla condimentum nulla.

~~~
section = content.newSection()
box = section.newMain()
~~~

## Morisawa 

Nam leo orci, condimentum vel nunc et, euismod varius nisl. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut id imperdiet elit. Nulla lacus nibh, dignissim ac quam sit amet, vulputate pulvinar nisl. Mauris viverra finibus interdum. 

~~~
box = box.newInfo()
~~~

Praesent efficitur arcu id libero vulputate tristique. Suspendisse lectus nisi, bibendum nec mauris at, vestibulum pulvinar sapien. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Suspendisse non libero in ex vestibulum bibendum sed sit amet lectus. Nullam aliquam laoreet fringilla. Phasellus ut diam accumsan, bibendum nisi sed, laoreet sem.

~~~
box = section.newSide()
~~~

* Cras vel leo sed turpis
* Bibendum tempus. 
* Vestibulum vitae porta urna. 
* Nunc pellentesque metus in nunc lobortis, sed finibus massa tincidunt. 
* Ut fringilla condimentum nulla.

~~~
section = content.newSection()
box = section.newMain()
~~~

## Sandoll

Nam leo orci, condimentum vel nunc et, euismod varius nisl. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut id imperdiet elit. 

~~~
box = box.newInfo()
~~~

Nulla lacus nibh, dignissim ac quam sit amet, vulputate pulvinar nisl. Mauris viverra finibus interdum. Praesent efficitur arcu id libero vulputate tristique. Suspendisse lectus nisi, bibendum nec mauris at, vestibulum pulvinar sapien. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Suspendisse non libero in ex vestibulum bibendum sed sit amet lectus. Nullam aliquam laoreet fringilla. Phasellus ut diam accumsan, bibendum nisi sed, laoreet sem.

~~~
box = section.newSide()
~~~

* Cras vel leo sed turpis
* Bibendum tempus. 
* Vestibulum vitae porta urna. 
* Nunc pellentesque metus in nunc lobortis, sed finibus massa tincidunt. 
* Ut fringilla condimentum nulla.

~~~
section = content.newSection()
box = section.newMain()
~~~

## Type Network

Nam leo orci, condimentum vel nunc et, euismod varius nisl. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut id imperdiet elit. Nulla lacus nibh, dignissim ac quam sit amet, vulputate pulvinar nisl. Mauris viverra finibus interdum. Praesent efficitur arcu id libero vulputate tristique. 

~~~
box = box.newInfo()
~~~

Suspendisse lectus nisi, bibendum nec mauris at, vestibulum pulvinar sapien. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Suspendisse non libero in ex vestibulum bibendum sed sit amet lectus. Nullam aliquam laoreet fringilla. Phasellus ut diam accumsan, bibendum nisi sed, laoreet sem.

~~~
box = section.newSide()
~~~

![w=450 y=top nocache](images/Typetr1.gif)

* Cras vel leo sed turpis
* Bibendum tempus. 

~~~
box = section.newMain()
~~~
## About this site

This site is generated by [PageBot](https://GitHub.com/PageBot/PageBot/blob/master/README.md), using a single MarkDown file as source. Learning how that works can be the topic of a study.

## Trademarks

Cras vel leo sed turpis bibendum tempus. Vestibulum vitae porta urna. Nunc pellentesque metus in nunc lobortis, sed finibus massa tincidunt. Ut fringilla condimentum nulla, eget convallis metus dapibus in. Vestibulum libero justo, cursus et purus vitae, ornare euismod nisi. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Phasellus vel mi quis tellus ultricies ultrices ut eu turpis. Sed ullamcorper eu erat vel dictum.


~~~
box = section.newSide()
~~~

## Links

* [typetr.typenetwork.com](http://typetr.typenetwork.com)
* [upgrade.typenetwork.com](http://upgrade.typenetwork.com)
* [bitcount.typenetwork.com](http://bitcount.typenetwork.com)

