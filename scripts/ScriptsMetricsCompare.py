from pagebot.fonttoolbox.objects.font import findFont
for fn in installedFonts():
    if 'Upgrade' in fn:
        print(fn)
        
fName = 'WorldFont-Regular'
fSlabName = 'WorldFontSlab-Regular'
fbuildName = 'UpgradeCJK-Regular'

latin = 'Travel' #'Hkpx'
kanji = "⽀⽌⽒⾄⽰⽽⽿⾃⿅⾞⼿⾸⾈"
chinese = "㟸㠆㟹㟽㟾㟿㠁㠂㠃㠈㠉㠊㠎㠏"
hangul = "ㅱㅸㅹㆄㆅㆆㆇㆈㆉㆊㆋ"

n = 2
sz = 120

s = FormattedString(latin + kanji[:n] + chinese[:n] + hangul[:n], font=fName, fontSize=sz  )
text(s, (50, 50))

s = FormattedString(latin + kanji[:n] + chinese[:n] + hangul[:n], font=fSlabName, fontSize=sz  )
text(s, (50, 250))

s = FormattedString(latin + kanji[:n] + chinese[:n] + hangul[:n], font=fbuildName, fontSize=sz  )
text(s, (50, 450))