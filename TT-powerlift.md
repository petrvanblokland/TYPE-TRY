
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
# More TYPETR PowerLift variants in the making. [TRY](downloads/PowerLift_Try.zip) them now.

~~~
box = content.newCropped(fill=0.3)
~~~
![x=center y=top contain noscale no-repeat](images/IMG_4664.JPG)

# Hey Bun, let’s get a Croque Monsieur

~~~
box = content.newIntroduction() # Large color background, white large text
~~~

# [TRY](downloads/PowerLift_Try.zip) the heavy weight PowerLift in your design work. Two variants are released: **PowerLift Tight** and **PowerLift Tight Outline**, matching to be used in layers. A new one is to be released in 2019: **PowerLift Tight Circle**.

~~~
box = content.newTypeList(doc.docLib['fontDataList']['PowerLift'], fontSize=44, labelFont='Upgrade-Regular', labelFontSize=18)

box = content.newBanner()
~~~

# What designers did with the font.

~~~
box = content.newWaterfall(doc.docLib['fontDataList']['PowerLift'], fontSizes=[48,54,60,66,72], labelFont='Upgrade-Regular', labelFontSize=18)
~~~
