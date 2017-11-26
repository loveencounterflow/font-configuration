#!/usr/bin/env python3

"""thx to https://stackoverflow.com/a/43072008"""

import sys
from fontTools.ttLib import TTFont

font = TTFont(sys.argv[1], 0, allowVID=0,
       ignoreDecompileErrors=True,
       fontNumber=0, lazy=True)

I_cp = ord('I')
M_cp = ord('M')
I_glyphid = None
M_glyphid = None
for table in font['cmap'].tables:
  for codepoint, glyphid in table.cmap.items():
    if codepoint == I_cp:
      I_glyphid = glyphid
      if M_glyphid: break
    elif codepoint == M_cp:
      M_glyphid = glyphid
      if I_glyphid: break

if (not I_glyphid) or (not M_glyphid):
  sys.stderr.write("Non-alphabetic font %s, giving up!\n" % sys.argv[1])
  sys.exit(3)

glyphs = font.getGlyphSet()
i = glyphs[I_glyphid]
M = glyphs[M_glyphid]
if i.width == M.width:
  print( '33631', 'font looks monospaced' )
  sys.exit(0)
else:
  print( '33631', 'font does not look monospaced' )
  sys.exit(1)


