from PIL import Image, ImageDraw, ImageFont
import textwrap, os

W=H=1024
BG=(247,244,238)
img=Image.new("RGB",(W,H),BG)
d=ImageDraw.Draw(img)

def font(path, size):
    return ImageFont.truetype(path, size)
BOLD="/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
REG="/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SERIFB="/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

NAVY=(16,32,56); RED=(178,34,52); GOLD=(201,150,44); WHITE=(255,255,255)

# Header
d.rectangle([0,0,W,168], fill=NAVY)
d.text((36,18), "THE WORLD IN ONE DAY", font=font(BOLD,26), fill=(150,190,235))
d.text((34,48), "Wednesday 18 November 2026", font=font(SERIFB,52), fill=WHITE)
d.text((36,118), "The day's world news in one picture  •  Diplomacy • War • Politics • Markets • Climate", font=font(REG,21), fill=(215,225,240))
d.rectangle([0,168,W,176], fill=RED)

panels=[
  dict(tag="SHENZHEN — APEC SUMMIT", color=(178,34,52), bg=(253,238,238),
       head="Xi & Putin meet;\nTrump lands for\n3-way talks",
       body="Xi Jinping and Vladimir Putin met in Shenzhen as APEC opened. Trump arrived for trilateral talks Thursday on Ukraine, Iran and trade."),
  dict(tag="UKRAINE — WAR", color=(28,88,160), bg=(235,242,252),
       head="Ukraine hits Kerch\nBridge for a\nsecond night",
       body="Kyiv struck the bridge linking Russia to Crimea again. Ukraine counted 141 drones overnight; 6 hurt in Dnipro."),
  dict(tag="GULF — STRAIT OF HORMUZ", color=(190,100,20), bg=(253,244,230),
       head="Ship attacked in\nHormuz; drones\nfired across Gulf",
       body="A ship was hit in the strait: 1 crew missing, 11 injured. Iran said it sent drones toward Kuwait; Bahrain intercepted attacks before dawn."),
  dict(tag="ALASKA — U.S. SENATE", color=(30,58,120), bg=(238,240,250),
       head="Peltola wins Alaska:\nSenate goes\n56–44 Democratic",
       body="Democrat Mary Peltola, a Yup'ik Alaska Native, beat Republican Sen. Dan Sullivan — first Alaska Native in the U.S. Senate (AP)."),
  dict(tag="GAZA — WINTER WARNING", color=(110,96,40), bg=(246,243,228),
       head="Ceasefire frays as\nwinter closes in\non displaced Gaza",
       body="950,000 displaced people in Gaza are on flood-prone ground in a fourth winter, UN agencies warn. The truce could collapse."),
  dict(tag="MARKETS & CLIMATE", color=(22,110,70), bg=(232,246,238),
       head="Nvidia beats;\nCOP31 climate talks\nnear the finish",
       body="Nvidia rose after strong results late Tuesday; Anthropic moved to price its IPO. COP31 negotiators in Antalya faced 144 disputed items."),
]

margin=28; gap=18
cols=2; rows=3
pw=(W-2*margin-(cols-1)*gap)//cols
top=192; bottom=944
ph=(bottom-top-(rows-1)*gap)//rows

def wrap(text, fnt, maxw):
    words=text.split(); lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if d.textlength(t, font=fnt) <= maxw: cur=t
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines

for i,p in enumerate(panels):
    r,c = divmod(i, cols)
    x=margin + c*(pw+gap); y=top + r*(ph+gap)
    # card
    d.rounded_rectangle([x,y,x+pw,y+ph], radius=14, fill=p["bg"], outline=p["color"], width=3)
    d.rounded_rectangle([x,y,x+pw,y+38], radius=14, fill=p["color"])
    d.rectangle([x,y+24,x+pw,y+38], fill=p["color"])
    d.text((x+14,y+8), p["tag"], font=font(BOLD,19), fill=WHITE)
    yy=y+50
    for line in p["head"].split("\n"):
        d.text((x+14,yy), line, font=font(BOLD,30), fill=NAVY)
        yy+=34
    yy+=4
    bf=font(REG,20)
    for line in wrap(p["body"], bf, pw-28):
        d.text((x+14,yy), line, font=bf, fill=(40,44,52))
        yy+=24

# Footer strip
d.rectangle([0,956,W,1024], fill=NAVY)
d.text((28,966), "ALSO ON 18 NOV:", font=font(BOLD,19), fill=(150,190,235))
d.text((28,990), "Quad leaders meet in Manila  •  Florida braces for catastrophic rain & flooding  •  EU proposes €45bn for Ukraine", font=font(REG,19), fill=WHITE)

out=os.path.expanduser("~/workspace/makefun-news-image-20261118/entry/entry.png")
img.save(out, optimize=True)
print(out, os.path.getsize(out), img.size)
