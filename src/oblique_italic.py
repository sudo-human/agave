import fontforge
import psMat
import math
import os


src_r = os.path.join(os.path.dirname(__file__), "agave-r.sfd")
src_i = os.path.join(os.path.dirname(__file__), "agave-i.sfd")

# All 95 printable ASCII glyphs
MISSING = [
    'space', 'exclam', 'quotedbl', 'numbersign', 'dollar', 'percent',
    'ampersand', 'quotesingle', 'parenleft', 'parenright', 'asterisk',
    'plus', 'comma', 'hyphen', 'period', 'slash', 'zero', 'one', 'two',
    'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'colon',
    'semicolon', 'less', 'equal', 'greater', 'question', 'at',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'bracketleft', 'backslash', 'bracketright', 'asciicircum', 'underscore',
    'grave', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'braceleft', 'bar', 'braceright', 'asciitilde',
]

# Shear matrix for ItalicAngle -10°: x' = x + y * tan(10°)
SHEAR = psMat.skew(math.radians(10))

font_r = fontforge.open(src_r)
font_i = fontforge.open(src_i)

added = 0
for name in MISSING:
    if name not in font_r:
        print("warning: '{}' not in Regular, skipping".format(name))
        continue

    gr = font_r[name]

    # Get or create the glyph slot in italic
    gi = font_i.createChar(gr.unicode, name)

    gi.width = gr.width
    gi.clear()

    pen = gi.glyphPen()
    gr.draw(pen)
    del pen

    gi.transform(SHEAR)

    added += 1
    print("  added: {}".format(name))

font_i.save(src_i)
font_r.close()
font_i.close()
print("\n{} glyphs added. Saved: {}".format(added, src_i))
