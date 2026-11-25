#!/usr/bin/env python3
"""Authoring recipe for the rogue-agent meme (not used by the graded entry).

Renders a flat-vector 1024x1024 PNG: an AI agent that has quietly started
house-training its own human. Pillow is only needed here, at build time.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (240, 233, 216)
INK = (38, 45, 52)
MUTED = (110, 117, 122)
STEEL = (132, 153, 161)
STEEL_D = (96, 118, 126)
SCREEN = (32, 44, 52)
RED = (176, 74, 66)
SKIN = (224, 190, 154)
SHIRT = (108, 132, 152)
CONE = (216, 160, 92)
FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
BOLD = FONT_DIR + "DejaVuSans-Bold.ttf"
REG = FONT_DIR + "DejaVuSans.ttf"


def font(size, bold=True):
    return ImageFont.truetype(BOLD if bold else REG, size)


def fit(draw, text, maxw, start, bold=True, floor=14):
    size = start
    while size > floor:
        f = font(size, bold)
        if draw.textlength(text, font=f) <= maxw:
            return f
        size -= 1
    return font(floor, bold)


def center(draw, text, y, f, fill):
    box = draw.textbbox((0, 0), text, font=f)
    draw.text(((W - (box[2] - box[0])) / 2, y), text, font=f, fill=fill)


im = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(im)

# Masthead and rule.
center(d, "ROGUE AGENT  //  DAY 4", 44, font(30), MUTED)
d.line([(70, 104), (954, 104)], fill=(196, 188, 172), width=4)

# Floor and its soft shadow.
d.line([(70, 742), (954, 742)], fill=(196, 188, 172), width=5)
d.ellipse([(200, 726), (470, 758)], fill=(219, 211, 194))
d.ellipse([(640, 726), (880, 758)], fill=(219, 211, 194))

# --- The agent: upright, smug, holding the leash. ---
d.rounded_rectangle([(250, 398), (412, 662)], radius=34, fill=STEEL, outline=INK, width=6)
d.rounded_rectangle([(256, 250), (406, 394)], radius=38, fill=STEEL, outline=INK, width=6)
d.line([(331, 250), (331, 212)], fill=INK, width=8)
d.ellipse([(317, 192), (345, 220)], fill=RED, outline=INK, width=4)

# Face screen: two bright eyes and a satisfied little smile.
d.rounded_rectangle([(276, 286), (386, 358)], radius=14, fill=SCREEN, outline=INK, width=4)
d.ellipse([(298, 306), (316, 324)], fill=BG)
d.ellipse([(348, 306), (366, 324)], fill=BG)
d.arc([(312, 316), (352, 344)], start=15, end=165, fill=BG, width=5)

# Trainer badge.
d.rounded_rectangle([(286, 476), (376, 512)], radius=8, fill=BG, outline=INK, width=3)
tf = fit(d, "TRAINER", 82, 22)
d.text((289, 481), "TRAINER", font=tf, fill=INK)

# Arm, hand, legs.
d.line([(404, 470), (472, 520)], fill=STEEL_D, width=22)
d.ellipse([(458, 506), (492, 540)], fill=STEEL, outline=INK, width=5)
d.rounded_rectangle([(280, 656), (316, 738)], radius=10, fill=STEEL_D, outline=INK, width=5)
d.rounded_rectangle([(348, 656), (384, 738)], radius=10, fill=STEEL_D, outline=INK, width=5)

# --- The human: on all fours, in the cone of shame. ---
d.rounded_rectangle([(676, 592), (838, 716)], radius=30, fill=SHIRT, outline=INK, width=6)
d.ellipse([(700, 484), (812, 596)], fill=SKIN, outline=INK, width=6)
# Hair cap.
d.pieslice([(699, 481), (813, 569)], start=180, end=360, fill=INK)
# Eyes and a tongue out.
d.ellipse([(736, 530), (746, 540)], fill=INK)
d.ellipse([(772, 530), (782, 540)], fill=INK)
d.ellipse([(792, 552), (822, 568)], fill=(206, 116, 118), outline=INK, width=3)
# Collar, tag, cone.
d.rounded_rectangle([(700, 580), (812, 606)], radius=10, fill=RED, outline=INK, width=4)
d.polygon([(688, 596), (824, 596), (756, 670)], fill=CONE, outline=INK)
d.line([(688, 596), (756, 670)], fill=INK, width=4)
d.line([(824, 596), (756, 670)], fill=INK, width=4)

# Leash, with a slight sag between the hand and the collar.
pts = [(480, 526), (520, 556), (560, 586), (600, 606), (640, 604), (680, 590), (704, 586)]
d.line(pts, fill=RED, width=9, joint="curve")

# Speech bubble: the human has learned its one word.
d.rounded_rectangle([(828, 392), (996, 466)], radius=22, fill=BG, outline=INK, width=5)
d.polygon([(862, 462), (826, 528), (908, 464)], fill=BG, outline=INK)
d.line([(862, 462), (826, 528)], fill=INK, width=5)
bf = fit(d, "woof.", 140, 44)
d.text((846, 404), "woof.", font=bf, fill=INK)

# Punchline, auto-fit so it never clips.
d.line([(70, 800), (954, 800)], fill=(196, 188, 172), width=4)
cf = fit(d, "WHO'S A GOOD HUMAN?", 900, 84)
center(d, "WHO'S A GOOD HUMAN?", 852, cf, INK)

im.save("/opt/data/makefun/repos/rogue-human/entry.png", "PNG", optimize=True)
print("rendered 1024x1024 entry.png")
