import polib
import os

FPATH = 'for_translation_sponsorcraft_primo_django_cy_GB.po'
FRAGS = 4

po = polib.pofile(FPATH)

# determine total character size of all the entries in the file
length = 0
for index, entry in enumerate(po):
    length += len(entry.msgid)

print 'count %s, size %s' % (index + 1, length)

# reopen as source for copying
po = polib.pofile(FPATH)
assert len(po)

# build a list of endpoints for the slices
ends = [0, len(po)]
fraglen = 0
for index, entry in enumerate(po):
    fraglen += len(entry.msgid)
    if fraglen >= length / FRAGS:
        fraglen = 0
        ends.insert(-1, index)

# ouput the files
for frag in range(FRAGS):
    pp = list(os.path.splitext(FPATH))
    pp.insert(1, '_%d' % frag)
    start, end = ends[frag:frag + 2]
    poslice = polib.POFile()
    poslice.metadata = po.metadata
    poslice.extend(po[start:end])
    poslice.save(''.join(pp))

print 'check the local directory for the split files.'
