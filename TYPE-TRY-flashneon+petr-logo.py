
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.contexts import getContext
from pagebot.document import Document
from pagebot.toolbox.units import degrees, em, pt
from pagebot.elements import *
from pagebot.toolbox.color import color

STEP = 4
FRAMES = int(350/STEP)
TRACK = em(0.4)

S = 1.5

W = pt(420)*S
H = pt(80)*S
M = 0
ML = 18
MM = 5*S

FONTSIZE = pt(60)*S

context = getContext()
f = findFont('Upgrade-Semibold')
print(f.features)

doc = Document(w=W, h=H, autoPages=FRAMES, frameDuration=0.2)
page = doc[1]

#c1 = color(0x42F1FF)
c1 = color(1, 1, 1)
c1a = color(c1.r, c1.g, c1.b, a=0.3)
c2 = color(0xFF0000)
c2a = color(0xFF0000, a = 0.2)

color1 = c1
color2 = c1
color3 = c1
color4 = c2a

petrOnly = True # Only once.

for frame in range(0, 360, STEP):
    if random() < 0.6:
        if random() < 0.5:
            color1 = c1
            color2 = c1
            color3 = c1
            color4 = c2a
        elif petrOnly:
            petrOnly = False
            color1 = c1a
            color2 = c1
            color3 = c1
            color4 = c2a  
        else:
            color1 = c1a
            color2 = c1a
            color3 = c2
            color4 = c2
        
    style1 = dict(font=f, fontSize=FONTSIZE, textFill=color1, tracking=TRACK)
    style2 = dict(font=f, fontSize=FONTSIZE, textFill=color2, tracking=TRACK)
    style3 = dict(font=f, fontSize=FONTSIZE, textFill=color3, tracking=TRACK)
    style4 = dict(font=f, fontSize=FONTSIZE, textFill=color4, tracking=0)
    bs = context.newString('TY', style=style1)
    bs += context.newString('PE', style=style2)
    bs += context.newString('TR', style=style3)
    bs += context.newString('Y', style=style4)
    newRect(parent=page, fill=0, w=W, h=H)
    newTextBox(bs, parent=page, x=ML, y=M-MM, w=W-ML-M, h=H+MM)
    if frame < 360-STEP:
        page = page.next
    
doc.export('images/TYPE-TRY-logo.gif')