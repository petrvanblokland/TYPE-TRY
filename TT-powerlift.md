
~~~
# ----------------------------------------
# Studies/2018-reviews.html
# ----------------------------------------
page = page.next
page.applyTemplate(template)  
page.name = 'PowerLift'
page.url = 'powerlift.html'

content = page.select('Content')
box = content.newBanner()
~~~
# Type in the making. Try it now.

~~~
box = content.newCropped()
~~~
![y=bottom](images/IMG_4664.JPG)

# Hey Bun, let’s get a Croque Monsieur

~~~
box = content.newIntroduction()
~~~

# TYPE-TRY gives an updated overview of running TYPETR projects. Download sample fonts to test yourself. Use the type already, while they are still in the making. Send wishes and suggestions. Find example templates that show we would use them. Copy code snippets to help you implement TYPETR type. 

~~~
content = page.select('Content')
box = content.newBanner()
~~~
# What designers did with the font

~~~
box = content.newTypeList(doc.docLib['fontDataList']['PowerLift'], fontSize=44, labelFont='Upgrade-Regular', labelFontSize=18)

box = content.newIntroduction()
~~~
# Nam leo orci, condimentum vel nunc et, euismod varius nisl. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut id imperdiet elit. 

~~~
section = content.newSection()
box = section.newMain()
~~~

## What we did…

* Nulla lacus nibh, dignissim ac quam sit amet, vulputate pulvinar nisl. 
* Mauris viverra finibus interdum. Praesent efficitur arcu id libero vulputate tristique. Suspendisse lectus nisi, bibendum nec mauris at, vestibulum pulvinar sapien. 
* Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Suspendisse non libero in ex 
* Vestibulum bibendum sed sit amet lectus. Nullam aliquam laoreet fringilla. Phasellus ut diam accumsan, bibendum nisi sed, laoreet sem.

~~~
box = section.newCropped()
~~~

![w=800 y=top x=center](images/habitCoverPagesSlab1-Chinese_1.gif)

~~~ 
section = content.newSection()
box = section.newMain()
~~~

# Best usage

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tincidunt neque ac neque iaculis feugiat. Praesent feugiat neque et sem gravida, vel mattis nibh tempus. 

![](images/IMG_4719.jpeg)

Suspendisse faucibus et lacus id vestibulum. Donec massa lacus, consectetur sit amet enim eu, vehicula vehicula quam. Aliquam erat volutpat. Quisque posuere tempor leo, in rhoncus diam volutpat ut. Nunc vitae sapien et urna ullamcorper maximus porta id urna. 

![](images/IMG_4814.jpeg)

Aliquam at ex aliquet, lacinia risus vel, rhoncus velit. Etiam id arcu mi. Nulla iaculis mi eu turpis viverra malesuada. Curabitur rhoncus est nec odio volutpat congue. Proin posuere nulla nunc, ac dictum ligula ullamcorper eget. Nullam et tempor lacus, et interdum leo. Nam faucibus sit amet mi sit amet imperdiet. Quisque cursus eros ligula, at laoreet arcu sagittis eget.

![](images/WF-bierCoverSlabPages2-All_1.png)

~~~
box = section.newSide()
~~~ 

![](images/fashionCoverPages1-Latin_1.png)
![](images/fashionCoverPages1-Hangul_1.png)
![](images/fashionCoverPages1-Kanji_1.png)
