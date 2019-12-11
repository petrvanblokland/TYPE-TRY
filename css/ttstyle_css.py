#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     nanostyle.css.py
#
#     CSS file as Python string. This avoids the use (and install of SCSS) and is
#     much more flexible, as it as adapt to conditions, calculation and the usage of
#     selections of Theme/Palette instances.
#
#     Since we'll be translating the ^(label)s directly by the theme.mood, all "%" 
#     should be escaped by a double "%%"
#
#     https://css-tricks.com/font-size-viewport-units/
#     https://css-tricks.com/almanac/properties/f/font-size/
#     https://css-tricks.com/books/volume-i/scale-typography-screen-size/

cssPy = """
body {
    background-color: #%(body.fill)s;
    color: #%(body.textFill)s;
    font-family: 'Upgrade-Regular', sans-serif;
    font-size: 17px;
    line-height: 1.4em;
    font-weight: normal; 
    letter-spacing: 0.025em;

    margin: 8px; /* Margin between all page content and window */
}
img {
    width: 100%%;
}
img.icon {
    width: 18px;
    height: 18px;
}
/* Upgrade supports these OT-features:
{   'liga': True, 'tnum': True, 'pnum': False, 'sups': False, 'sinf': False, 'frac': False, 
    'zero': False, 'onum': True, 'lnum': False, 'vpal': True, 'case': False, 'ss08': False, 
    'ss09': False, 'ss10': False, 'smcp': False, 'c2sc': False
}
*/
span.case {
    -moz-font-feature-settings: 'case';    
    -webkit-font-feature-settings: 'case';
    font-feature-settings: 'case' on;
}
span.c2sc {
    -moz-font-feature-settings: 'c2sc';    
    -webkit-font-feature-settings: 'c2sc';
    font-feature-settings: 'c2sc' on;
}

/* Cropped texts */
div.upgrade-try-light-italic div h1 { /* H1 overlay on cropped photo */
    font-family: "Upgrade-LightItalic";
    font-size: 6em;
    line-height: 1.1;
    color: white;
    text-align: center;
}
/* Cropped texts */
div.upgrade-try-light div h1 { /* H1 overlay on cropped photo */
    font-family: "Upgrade-Light";
    font-size: 6em;
    line-height: 1.1;
    color: white;
    text-align: center;
}

/* Icons */
span.try-icon {
    font-family: "Upgrade-Medium";
    color: white;
    font-size: 0.9em;
    background-color: #FF0000;
    padding: 0.07em 0.2em 0 0.2em;
}
span.buy-icon {
    font-family: "Upgrade-Medium";
    color: white;
    font-size: 0.9em;
    background-color: #080833;
    padding: 0.07em 0.2em 0 0.2em;
}
span.tn-icon {
    font-family: "Upgrade-Medium";
    color: white;
    font-size: 0.9em;
    background-color: black;
    padding: 0.07em 0.2em 0 0.2em;
}
span.typetr-icon {
    font-family: "Upgrade-Medium";
    color: white;
    font-size: 0.9em;
    letter-spacing: -0.125em;
    background-color: #221188;
    padding: 0.07em 0.3em 0 0.18em;
}
span.google-icon {
    font-family: "Upgrade-Medium";
    color: white;
    font-size: 0.9em;
    background-color: #110055;
    padding: 0.07em 0.2em 0 0.2em;
}
img.adobe-icon {
    vertical-align: middle;
    height: 1.1em; /* 123px x 109px */
    width: 1.3em;
}

p {
    font-size: 1em;
    font-family: 'Upgrade-Regular';
}
p em {
    font-style: normal;
    font-family: 'Upgrade-RegularItalic';
}
p strong, li strong {
    font-weight: normal;
    font-family: 'Upgrade-Semibold';    
}
a {
    text-decoration: none;
    color: #%(p.textLink)s;
}
a:hover {
    text-decoration: none;
    color: #%(p.textHover)s;
    background-color: #%(p.fill)s;
}
ul {
    padding: 0 0 0 20px;
}

/* Heading */

h1, h2, h3, h4, h5, h6 {
    font-weight: normal;
    font-family: 'Upgrade-Regular', sans-serif;
    margin: .45em 0;
    padding: 0; 
}
h1 {font-size: 2em; line-height: 1.2em;}
h2 {font-size: 1.75em; line-height: 1.2em;}
h3 {font-size: 1.5em; line-height: 1.2em;}
h4 {font-size: 1.25em; line-height: 1.2em;}
h5 {font-size: 1em; line-height: 1.2em;}
p {font-size: 1em; line-height: 1.4em;}

h1 {
    font-family: 'Upgrade-Semibold', sans-serif;
    margin: 0;
    color: #%(h1.textFill)s;
}
h1 a {
    color: #%(h1.textLink)s;
}
h1 a:hover {
    color: #%(h1.textHover)s;
    background-color: none;
}

h2 a {
    color: #%(h2.textLink)s;
    background-color: none;
}
h2 a:hover {
    color: #%(h2.textHover)s;
    background-color: none;
}

h3 a {
    color: #%(h3.textLink)s;
    background-color: none;
}
h3 a:hover {
    color: #%(h3.textHover)s;
    background-color: none;
}

h4 a {
    color: #%(h4.textLink)s;
    background-color: none;
}
h4 a:hover {
    color: #%(h4.textHover)s;
    background-color: none;
}

h5 a {
    color: #%(h5.textLink)s;
    background-color: none;
}
h5 a:hover {
    color: #%(h5.textHover)s;
    background-color: none;
}

/* Debugging */
.cssId { /* Debug showing e.cssId */
    font-size: 1em;
    color: yellow;
    background-color: red;
}

/* Overall layout */
.wrapper, .content, .footer {
    display: grid;
    grid-template-columns: 1fr;
    column-gap: 10px;
    row-gap: 10px;
    background-color: #%(page.fill)s;    
}
.header {
    display: block;
    background-color: #%(page.fill)s;    
}
.clearfix {
  overflow: auto; /* CSS hack to grow div including all child content. */
}
.textbox {
    width: 100%%;
}

/* Logo */
.logo {
    float: left;
    width: 30%%;
    padding: 0.5em 0 0 1em;
}
.logo h1 {
    font-size: 2em;
    font-family: 'Upgrade-Medium';
    letter-spacing: 0.015em;
    color: #%(logo.textFill)s;
}

/* Rulers */

.main hr {
    border: 8px solid #%(hr2.stroke)s;
}
.side hr {
    border: 1px solid #%(hr2.stroke)s;
}

/* Desktop navigation/menu */

nav.navigation {
    float: right;
    width: 60å%%;
    padding: 0.75em 1em 0 0;
    z-index: 1000;
}

.navigation-menu {
    float: right;
    /* overflow: auto; CSS hack to grow div including all child content. */
}
ul.navmenu {
    list-style: none;
    padding: 0;
    margin: 0;
    background-color: #%(menu.fill)s;
}

ul.navmenu li {
    display: block;
    position: relative;
    float: left;
    background: #%(menu.fill)s;
}

li ul.navmenu { 
    display: none; 
    z-index: 1000;
}

li:hover > ul.navmenu { 
    display: block;
    position: absolute; 
}

ul.navmenu li a {
    display: block;
    padding: 6px 12px;
    text-decoration: none;
    white-space: nowrap;
    color: #%(menu.textLink)s;
    margin-right: 0px;
}

ul.navmenu li a:hover { 
    color: #ccc;
    background-color: #%(menu.textHover)s;
}

li:hover ul.navmenu {
    display: block;
    position: absolute;
}

/*
li:hover li { 
    float: none; 
}
*/
li:hover a { 
    background-color: #%(menu.fill)s; 
}

li:hover li a:hover { 
    background-color: #%(menu.fill)s; 
    color: #%(li.textHover)s;
}

.main-navigation li ul.navmenu li { 
    border-top: 0; 
}

/* 80%% to prevent menu's running off from the right side? */
ul.navmenu ul.navmenu ul.navmenu {
    left: 100%%;
    top: 0;
    margin-right: 
}

ul.navmenu:before,
ul.navmenu:after {
  content: " "; /* 1 */
  display: table; /* 2 */
}

ul.navmenu:after { 
    clear: both; 
}

/* Mobile menu and BurgerButton */

.menu {
}
.burgerbutton {
    float: right;
    display: none;
    padding-top: 0.5em;
}
.mobilemenu {
    display: none;
}
.mobilemenu .button, .mobilemenu .button2 {
    color: #%(mobilemenu.textLink)s;
    background-color: #%(mobilemenu.fill)s;
    border: none;
    width: 100%%;
    margin: 2px 0;
    padding: 6px;
    text-align: center;
    text-decoration: none
    display: inline-block;
    font-size: 3em;
    font-family: 'Upgrade-Medium', sans-serif;
}
.mobilemenu .button2 {
    color: #%(base3)s;
    font-size: 2em;
    padding: 5px;
    font-family: 'Upgrade-MediumItalic', sans-serif;
}


/* Banner on full width */
.banner {
    padding: 6pt 0;
    margin: 6pt 0 6pt 0;
    background-color: #%(banner.fill)s;
}
.banner .textbox h1 {
    font-size: 3em;
    line-height: 1.3em;
    font-family: 'Upgrade-Regular', sans-serif;
    color: #%(banner.textFill)s;
}
.banner .textbox h1 a { /* TRY Link in headlines */
    font-size: 0.75em;
    line-height: 1.3em;
    background-color: #%(banner.textFill)s;
    font-family: 'Upgrade-Medium', sans-serif;
    color: white;
    padding: 0.2em;
}
.banner .textbox h1 a:hover { 
    color: #DDD;
}

/* Collection */

.collection {
    background-color: #%(collection.fill)s;
}
.collectionelement{
    margin: 6px 2px 0 0;
    /* Width is defined by collection container
    depending on the amount of child elements. */
}

.introduction {
    background-color: #%(intro.fill)s;
    padding: 1em;
}
.introduction .textbox h1 {
    font-size: 3em;
    line-height: 1.2em;
    font-family: 'Upgrade-Book', sans-serif;
    color: #%(intro.textFill)s;
}
.introduction .textbox h1 a {
    font-family: 'Upgrade-Book', sans-serif;
    color: #%(intro.textLink)s;
}
.introduction .textbox h1 a:hover {
    color: #%(intro.textHover)s;
}

/* TypeList */
.typelistline .label {
    margin-top: 1em;
    margin-bottom: 1em;
}

/* Slide show */

.slideshowgroup {
    display: grid;
    grid-template-columns: 2fr 1fr;
    column-gap: 10px;
    row-gap: 10px;    
    background-color: #%(group.fillDiap)s;
}
.slideshow {
    background-color: #%(group.fillDiap)s;
}
.slideside {
    background-color: #%(group.fillDiap)s;
    padding: 0 1em 1em 0;
}
.slideside .textbox h1 {
    color: #%(h2.textFillDiap)s;
    letter-spacing: 0.025em;
    font-size: 1.4em;
    line-height: 1.2em;
    font-family: 'Upgrade-Regular';
}
.slideside .textbox h1 a {
    color: #%(base3)s;
}
.slideside .textbox h1 a:hover {
    color: #%(base3.colorFront)s;
}
.slideside .textbox h2 {
    color: #%(h2.textFillDiap)s;
    letter-spacing: 0.025em;
    font-size: 1.4em;
    line-height: 1.2em;
    font-family: 'Upgrade-Regular';
}
.slideside .textbox h3 {
    color: #%(h3.textFillDiap)s;
    letter-spacing: 0.025em;
    font-size: 1.1em;
    line-height: 1.2em;
    font-family: 'Upgrade-Medium';
}
.slideside .textbox p {
    color: #%(p.textFillDiap)s;
    letter-spacing: 0.025em;
    font-size: 1em;
    line-height: 1.4em;
    font-family: 'Upgrade-Regular';
}
.slideside .textbox p em {
    fony-style: normal;
    font-family: 'Upgrade-RegularItalic';
}

sup { /* Superior number <sup> by Upgrade OT-feature */
    top: 0em;
    color: #%(p.textFill)s;
    font-size: inherit;
    vertical-align: inherit;
    -moz-font-feature-settings:"sups=1";
    -moz-font-feature-settings:"sups";
    -ms-font-feature-settings:"sups";
    -webkit-font-feature-settings:"sups";
    font-feature-settings:"sups";
}
h1 sup { /* Superior Scale number in h1 */
    color: #%(h1.textFill)s;
}
li sup { /* Superior Scale number in Menu */
    color: #%(li.textFill)s;
}

/* Content */

.content {
    padding:1em;
}
.caption .textbox {
    font-family: 'Upgrade-RegularItalic';
    font-size: 1em;
    line-height: 1.4em;
}
.section {
    display: grid;
    grid-template-columns: 2fr 1fr;
    column-gap: 10px;
    row-gap: 10px;
    background-color: #%(base2.colorBack)s;
}
.mains {
    display: grid;
    grid-template-columns: 1fr;
    column-gap: 10px;
    row-gap: 10px;    
}
.main {
    padding: 0 %(side.pr)s;
    border-top: 15px solid #%(hr.stroke)s;
}
.sides {
    display: grid;
    grid-template-columns: 1fr;
    column-gap: 10px;
    row-gap: 10px;    
}
.side {
    padding: 0 %(side.pr)s;
    border-top: 15px solid #%(hr.stroke)s;
}

/* Cropped has attribute background-image and optional
floating elements inside.*/
.cropped {
    padding: 0 2em 20em 2em;
    border-top: 15px solid #%(hr.stroke)s;
}

/* Info area, open/clode by button */
.info {
    margin: 0;
    padding: 0;
}
.info-opened{
    display: none;    
}
.info-closed{
    display: block;   
}
.info-doopen, .info-doclose { /* [?] button, [x] button */
    float: right;
    margin: 0;
    text-align: center;
    padding: 0.2em 0.5em;
    height: 1em;
    width: 1em;
    font-size: 1.5em;
    background-color: #%(base3)s; /* Buttons in logo color */
    color: #%(base3.colorMostBack)s;
}


.footer {
    
}

/****************************************
*****************************************
MEDIAQUERIES
*****************************************
****************************************/

@media only screen and (max-width: 800px) {
    body {
        /*background-color: red;*/
        margin: 0;
    }
    h1 {font-size: 2.4em; line-height: 1.15em;}
    h2 {font-size: 2.2em; line-height: 1.15em;}
    h3 {font-size: 1.8em; line-height: 1.15em;}
    h4 {font-size: 1.4em; line-height: 1.15em;}
    h5 {font-size: 1.25em; line-height: 1.15em;}
    p, li {font-size: 1.25em; line-height: 1.3em;}

    .logo {
        width: 80%%;
    }
    .logo h1 {
        font-size: 1.5em;
    }

    .burgerbutton {
        float: right;
        display: block;
        margin-right: 12pt;
    }

    nav.navigation {
        display: none;
    }     
    .menu {
        display: none;
    }
    .mobilemenu {
        float: left;
        width: 100%%;
        display: none;
    }
    .mobilemenu .button {
        font-size: 2em;
    }
    .mobilemenu .button2 {
        font-size: 1.5em;
    }
    .banner .textbox h1 {
        font-size: 2.4em;
        line-height: 1.15em;
    }
    .banner .textbox h2 {
        font-size: 2.2em;
        line-height: 1.15em;
    }
    .banner .textbox p {
        font-size: 1.25em;
        line-height: 1.3em;
    }
    .slideshowgroup {
        grid-template-columns: 1fr;
    }
    .slideside {
        padding-left: 12pt;
        padding-right: 12pt;
    }
    .slideside .textbox p {
        font-size: 1.25em;
        line-height: 1.3em;
    }
    .introduction .textbox h1 {
        font-size: 2em;
        line-height: 1.15em;
    }
    .caption .textbox {
        font-family: 'Upgrade-RegularItalic';
        font-size: 1.25em;
        line-height: 1.3em;
    }
    .section {
        display: grid;
        grid-template-columns: 1fr;
    }

    /* Cropped texts */
    .cropped {
        /*height: 60vw; /* 60%% of view-port width. */
        border-top: none;
    }
    div.cropped div h1 { 
        font-size: 3.5em;
    }

    span.try-icon, span.buy-icon, span.tn-icon, span.typetr-icon, span.google-icon {
        font-size: 2.5em;
    }
    span.icon-label {
        display: none;
    }
    img.adobe-icon {
        vertical-align: bottom;
        height: 2.8em; /* 2.5em --> 123px x 109px */
        width: 3.6em;
    }

    /* TypeList */
    div.typelistline div.sample {
        font-size: 4em;
        color: red;
    }
}
@media only screen and (min-width: 800px) {
    body {
        /*background-color: cyan;*/
    }
    h1 {font-size: 3em; line-height: 1.2em;}
    h2 {font-size: 2em; line-height: 1.2em;}
    h3 {font-size: 1.6em; line-height: 1.2em;}
    h4 {font-size: 1.25em; line-height: 1.2em;}
    h5 {font-size: 1em; line-height: 1.2em;}
    p, li {font-size: 1em; line-height: 1.4em;}

    .header {
        grid-template-columns: 1fr 2fr;
    } 
    .logo h1 {
        font-size: 1.6em;
    }
    .navigation {
        display: block;
    }
    .burgerbutton, .mobilemenu {
        display: none;
    }

    .banner .textbox h1 {
        font-size: 3em;
        line-height: 1em;
    }
}
@media only screen and (min-width: 1000px) {
    body {
        /*background-color: orange;*/
    }
    .header {
        grid-template-columns: 2fr 3fr;
    } 
    .logo h1 {
        font-size: 2em;
    }
 
    .navigation {
        display: block;
    }
    .burgerbutton, .mobilemenu {
        display: none;
    }

    .banner .textbox h1 {
        font-size: 2.5em;
        line-height: 1.1em;
    }
}
@media only screen and (min-width: 1200px) {
    body {
        /*background-color: blue;*/
    }
    .wrapper {
        width: 1200px;
        margin: auto;
    } 
    .navigation {
        display: block;
    }
    .burgerbutton, .mobilemenu {
        display: none;
    }
}

/* PRINT STYLESHEET */
@media print {
  * { background: transparent !important; color: black !important; text-shadow: none !important; filter:none !important; -ms-filter: none !important; } /* Black prints faster: h5bp.com/s */
  a, a:visited { text-decoration: underline; }
  a[href]:after { content: " (" attr(href) ")"; }
  abbr[title]:after { content: " (" attr(title) ")"; }
  .ir a:after, a[href^="javascript:"]:after, a[href^="#"]:after { content: ""; }  /* Don't show links for images, or javascript/internal links */
  pre, blockquote { border: 1px solid #999; page-break-inside: avoid; }
  thead { display: table-header-group; } /* h5bp.com/t */
  tr, img { page-break-inside: avoid; }
  img { max-width: 100%% !important; }
  @page { margin: 0.5cm; }
  p, h2, h3 { orphans: 3; widows: 3; }
  h2, h3 { page-break-after: avoid; }
"""
