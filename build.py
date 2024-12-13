#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#   T Y P E T R . C O M
#
#   Copyright (c) 2020+ Buro Petr van Blokland + Claudia Mens
#
#   build.py
#
#   Source builds the type-try.com website using PageBotNano the Website 
#   publication class.
#
#   https://docs.fontdue.com
#   https://typetr.fontdue.com/admin/settings/website
#
#   http://localhost/typetr/index.html
#   https://petrvanblokland.github.io/TYPE-TRY/index.html
#
#
import os, shutil, codecs

URL = 'typetr.com'

USE_MAMP = True

EXPORT_PATH = 'docs/'
ASSETS_PATH = 'assets/'
FONTS_PATH = 'fonts/'
IMAGES_PATH = 'images/'
MAMP_PATH = '/Users/petr/Sites/localhost/typetr'
TEMPLATE_PATH = 'templated-binary/'

# Key values replace the {{key}} references in the templated-binary/index.html templates. 
CONTENT = {
    'logo': '<img src="images/type-try-logo.gif", width="50%"/>',
    'menuPageLinks': 'menuPageLinks',
    'pageTitle': 'getPageTitle',
    'collection-id': 'getCollectionId'
}  

class Page:

    def __init__(self, name, templateName=None, id=None, collectionId=None):
        self.name = name    
        self.templateName = templateName or name
        self.id = id or name
        self.collectionId = collectionId or ''
        self.readTemplate(self.templateName)

    def readTemplate(self, templateName):
        f = codecs.open(f'{TEMPLATE_PATH}{templateName}.html', 'r', encoding='UTF-8')
        self.html = f.read()
        f.close()

    # Content methods

    def getPageTitle(self, pages):
        return self.name

    def getCollectionId(self, pages):
        return self.collectionId

    def menuPageLinks(self, pages):
        html = ''
        for page in pages:
            html += f'\t\t<li><a href="{page.name.lower()}.html">{page.name}</a></li>\n'
        return html

    def buildContent(self, pages):
        for key, content in CONTENT.items():
            if hasattr(self, content):
                content = getattr(self, content)(pages)
            elif hasattr(self, key): # Does it exist a method, then do the call.
                content = getattr(self, key)(pages)
            
            self.html = self.html.replace('{{' + key + '}}', content)

    def build(self, pages):
        self.buildContent(pages)
        f = codecs.open(f'{EXPORT_PATH}{self.name.lower()}.html', 'w', encoding='UTF-8')
        f.write(self.html)
        f.close()

class Site:

    def __init__(self, url, id):
        self.url = url
        self.id = id
        self.pages = []

    def appendPage(self, page):
        self.pages.append(page)

    def copyDir(self, path1, path2):
        shutil.copytree(path1, path2)

    def build(self):
        if os.path.exists(EXPORT_PATH):
            shutil.rmtree(EXPORT_PATH)
            os.mkdir(EXPORT_PATH)

        self.copyDir(ASSETS_PATH, EXPORT_PATH + ASSETS_PATH)
        self.copyDir(FONTS_PATH, EXPORT_PATH + FONTS_PATH)
        self.copyDir(IMAGES_PATH, EXPORT_PATH + IMAGES_PATH)

        for page in self.pages:
            page.build(self.pages)

        # Write the CNAME file
        f = codecs.open(f'{EXPORT_PATH}CNAME', 'w', encoding='UTF-8')
        f.write(URL)
        f.close()

#PORT = 8888
PORT = 80

site = Site('typetr', 'typetr')

# Pagename, template name
site.appendPage(Page('Index', 'index'))

site.appendPage(Page('Presti', 'index', collectionId='Presti Display'))
site.appendPage(Page('Proforma Pro', 'index'))
site.appendPage(Page('Powerlift', 'index'))
site.appendPage(Page('MyNewTYpeface', 'index'))
site.appendPage(Page('Responder', 'index'))
site.appendPage(Page('Upgrade', 'index'))
site.appendPage(Page('Upgrade Neon', 'index'))
site.appendPage(Page('Upgrade Outline', 'index'))
site.appendPage(Page('About TYPETR', 'index'))
site.appendPage(Page('Contact', 'index'))
site.appendPage(Page('ZZZZZZZ', 'index'))

site.build()

if USE_MAMP:
    # Start MAMP to see this website on localhost, port 80
    # Since we modify the 'docs/', better make a tree copy than exporting again.
    mampPath = MAMP_PATH #+ site.id
    if os.path.exists(mampPath):
        print('... Remove old site at', mampPath)
        shutil.rmtree(mampPath)
    shutil.copytree('docs/', mampPath)
    #website.export(mampPath)

    # Open the local website on docs/, assuming that MAMP is running
    os.system(u'/usr/bin/open %s/%s' % (site.url, site.id))

print('Done')