#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#   P A G E B O T  N A N O
#
#   Copyright (c) 2020+ Buro Petr van Blokland + Claudia Mens
#   www.pagebot.io
#   Licensed under MIT conditions
#
#   Supporting DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#   build.py
#
#   Source builds the type-try.com website using PageBotNano the Website 
#   publication class.
#
import os, shutil, codecs

from typetrydata import siteData # Content data instances for this site
from pagebotnano_060.toolbox.loremipsum import loremipsum, randomName, randomTitle
from pagebotnano_060.templates.templated import * # Import all templates classes.
from pagebotnano_060.themes import BackToTheCity
from pagebotnano_060.toolbox.markdown import parseMarkdownFile
from pagebotnano_060.publications.website import Website

SRC_FONTS_PATH = '../TYPE-TRY-Sources/'
SRC_FONTS_PATHS = (
    'Bitcount-Outline/Bitcount-Outline-web/', # Full Open Source version, no TRY
    'Presti/Presti-web/', 
    'PowerLift/PowerLift-web/', 
    'Responder-P/Responder-P-web/', 
    #'Proforma-Pro/Proforma-Pro-web/', 
    'Upgrade/Upgrade-web/'
)
DST_FONTS_PATHS = (
    'fonts/', 
    'docs/assets/fonts/'
) 
SRC_ZIP_FONTS_PATHS = (
    'Bitcount-Outline/Bitcount-Outline.zip', # Full Open Source version, no TRY
    'Presti/Presti-TRY.zip', 
    'PowerLift/PowerLift-TRY.zip', 
    'Responder-P/Responder-P-TRY.zip', 
    #'Proforma-Pro/Proforma-Pro-TRY.zip', 
    'Upgrade/Upgrade-TRY.zip'
)
DST_ZIP_FONTS_PATHS = (
    'fonts-try/', 
    'docs/assets/fonts-try/'
) 
CSS_FONT_PATHS = (
    'docs/assets/css/webfonts.css',
)

#PORT = 8888
PORT = 80

class TypeTryTemplate(TemplatedHielo):
    pass


# Create a Website publications with this theme and templates
#templates = TemplatedBinary()
#templates = TemplatedBroadcast()
#templates = TemplatedCaminar()    'images/lookbook/
#templates = TemplatedFullmotion()
#templates = TemplatedInterphase()
#templates = TemplatedIntrospect()
#templates = TemplatedRoadtrip()
#templates = TemplatedTheory()
#templates = TemplatedSnapshot()
#templates = TemplatedRadius()

templates = TypeTryTemplate()

website = Website(templates=templates, port=PORT)
website.templates.read('images')

# Compose the website with this content.
website.compose(siteData)

# Export website to docs/, so it will be published as site 
# by github under https://type-try.com
website.export('docs/') 

# Clear folders that will contain webfonts
for dstPath in []: #DST_FONTS_PATHS:
    for fontName in os.listdir(dstPath):
        if not fontName.startswith('.'):
            os.remove(dstPath + fontName)

# Copy fonts to fonts-try (zip) and fonts-web
# and while scanning through, generate the font.css file.

# Open css file 
css = []
CSS_FONT_TEMPLATE = """
@font-face {
  font-family: "%(fontName)s";
  src: url("../fonts/%(fontName)s.woff2") format("woff2"),
       url("../fonts/%(fontName)s.woff") format("woff");
}
"""

for relSrcPath in SRC_FONTS_PATHS:
    srcPath = SRC_FONTS_PATH + relSrcPath
    if not os.path.exists(srcPath):
        print('### Missing', srcPath)
        continue
    cssDone = set()
    for dstPath in DST_FONTS_PATHS:
        for srcFontName in os.listdir(srcPath):
            if srcFontName.startswith('.'):
                continue
            srcFilePath = srcPath + srcFontName
            shutil.copyfile(srcFilePath, dstPath + srcFontName)
            if srcFontName.endswith('woff2'):
                cssFontKey = srcFontName.replace('.woff2', '')
                if cssFontKey not in cssDone:
                    css.append(CSS_FONT_TEMPLATE % dict(fontName=cssFontKey))
                    cssDone.add(cssFontKey)
                    
# Write the generate font css to webfonts.css files.
for cssPath in CSS_FONT_PATHS:
    print('... Write %s' % cssPath)
    cssFile = codecs.open(cssPath, 'w', encoding='utf-8')
    cssFile.write(''.join(css))
    cssFile.close()

# Copy zipped TRY fonts for downloading
for fileName in SRC_ZIP_FONTS_PATHS:
    filePath = SRC_FONTS_PATH + fileName
    if not os.path.exists(filePath):
        print('### Missing', filePath)
        continue

    for dstPath in DST_ZIP_FONTS_PATHS:
        shutil.copyfile(filePath, dstPath + fileName.split('/')[-1])

# Start MAMP to see this website on localhost, port 80
# Since we modify the 'docs/', better make a tree copy than exporting again.
mampPath = website.MAMP_PATH + siteData.id
if os.path.exists(mampPath):
    print('... Remove old site at', mampPath)
    shutil.rmtree(mampPath)
print('... Copy site as', siteData.id, 'to MAMP', mampPath)
shutil.copytree('docs/', mampPath)
#website.export(mampPath)


# Open the local website on docs/, assuming that MAMP is running
print('... Opening site %s on %s' % (siteData.id, website.url))
os.system(u'/usr/bin/open %s/%s' % (website.url, siteData.id))

print('Done')