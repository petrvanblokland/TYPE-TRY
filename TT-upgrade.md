~~~
# ----------------------------------------
# upgrade.html
# ----------------------------------------
page = page.next
page.applyTemplate(template)  
page.name = 'Upgrade'
page.url = 'upgrade.html'

content = page.select('Content')
box = content.newBanner()
~~~
# More <span class="c2sc">TYPETR</span> Upgrade variants in the making. [TRY](downloads/TYPETR_Upgrade_Try-ttf.zip) them now.

~~~
box = content.newCropped(fill=0.3, cssClass='cropped upgrade-try-light')
~~~
![x=center y=top contain noscale no-repeat](images/IMG_4664.JPG)

# You & me will have a romantic <span class="c2sc">DINER</span> night.

~~~
box = content.newIntroduction()
~~~

# <span class="case">TYPE-TRY</span> gives an updated overview of running <span class="c2sc">TYPETR</span> projects. Download sample fonts to test in your designs. Use the type, while it is still in the making. Express wishes and suggestions. Find example templates. Get code snippets that best implement TYPETR type.

~~~
# The Upgrade-Try fontDataList is defined by the calling application.
box = content.newTypeList(doc.docLib['fontDataList']['Upgrade Try'], fontSize=44, leading=em(1), labelFont='Upgrade-Regular', labelFontSize=18)

box = content.newCropped(fill=0.3, cssClass='cropped upgrade-try-light-italic')
~~~
![x=center y=top contain noscale no-repeat](images/IMG_4609.JPG)

# Sweetheart, it’s hotdog time.

~~~
# The Upgrade-Try fontDataList is defined by the calling application.
box = content.newTypeList(doc.docLib['fontDataList']['Upgrade Try Italic'], fontSize=44, leading=em(1), labelFont='Upgrade-Regular', labelFontSize=18)

box = content.newWaterfall(doc.docLib['fontDataList']['Upgrade Waterfall'], fontSizes=[11,12,13,14,15,16,18], labelFont='Upgrade-Regular', labelFontSize=18)

~~~
