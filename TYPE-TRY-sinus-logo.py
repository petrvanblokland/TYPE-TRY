
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.contexts import getContext
from pagebot.document import Document
from pagebot.toolbox.units import degrees, em, pt
from pagebot.elements import *
from pagebot.toolbox.color import color

STEP = 5
FRAMES = int(350/STEP)
TRACK = em(0.4)

W = pt(420)
H = pt(80)
M = 0
ML = 18

FONTSIZE = pt(60)

context = getContext()
f = findFont('Upgrade-Semibold')
print(f.features)

doc = Document(w=W, h=H, autoPages=FRAMES, frameDuration=0.05)
page = doc[1]

c1 = color(0x42F1FF)
c2 = color(0xFF0000)

for frame in range(0, 360, STEP):
    a = degrees(frame).sin*0.5+0.5
    color1 = c1
    color2 = color(c1.r*a + c2.r*(1-a), c1.g*a + c2.g*(1-a), c1.b*a + c2.b*(1-a),)
    color3 = color(c2.r, c2.g, c2.b, a=(1-a))
    style1 = dict(font=f, fontSize=FONTSIZE, textFill=color1, tracking=TRACK)
    style2 = dict(font=f, fontSize=FONTSIZE, textFill=color2, tracking=TRACK)
    style3 = dict(font=f, fontSize=FONTSIZE, textFill=color3, tracking=0)
    bs = context.newString('TYPE', style=style1)
    bs += context.newString('TR', style=style2)
    bs += context.newString('Y', style=style3)
    newRect(parent=page, fill=0, w=W, h=H)
    newTextBox(bs, parent=page, x=ML, y=M-5, w=W-ML-M, h=H+5)
    if frame < 360-STEP:
        page = page.next
    
doc.export('_export/TYPE•TRY-logo.gif')