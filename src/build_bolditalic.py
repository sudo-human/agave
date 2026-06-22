import fontforge
import os

src = os.path.join(os.path.dirname(__file__), "agave-z.sfd")
raw = os.path.join(os.path.dirname(__file__), "..", "dist", "Agave-BoldItalic-raw.ttf")

font = fontforge.open(src)
font.generate(raw, flags=("opentype", "PfEd-comments"))
font.close()
print("Generated:", raw)
