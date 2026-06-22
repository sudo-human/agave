import fontforge
import psMat
import math
import os

src_b = os.path.join(os.path.dirname(__file__), "agave-b.sfd")
src_z = os.path.join(os.path.dirname(__file__), "agave-z.sfd")

# All 95 printable ASCII glyphs + non-breaking space
GLYPHS = [
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
    'braceleft', 'bar', 'braceright', 'asciitilde', 'uni00A0',
]

# Shear matrix for ItalicAngle -10°: x' = x + y * tan(10°)
SHEAR = psMat.skew(math.radians(10))

font_b = fontforge.open(src_b)
font_z = fontforge.open(src_z)

added = 0
for name in GLYPHS:
    if name not in font_b:
        print("warning: '{}' not in Bold, skipping".format(name))
        continue

    gb = font_b[name]

    gz = font_z.createChar(gb.unicode, name)

    gz.clear()

    pen = gz.glyphPen()
    gb.draw(pen)
    del pen

    gz.width = gb.width
    gz.transform(SHEAR)

    added += 1
    print("  added: {}".format(name))

font_z.save(src_z)
font_b.close()
font_z.close()
print("\n{} glyphs added. Saved: {}".format(added, src_z))
