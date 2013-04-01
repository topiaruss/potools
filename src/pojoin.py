import polib
import os
import sys

OUT = 'out.po'

files = sys.argv[1:]
print files


out = polib.POFile()

for f in files:
    po = polib.pofile(f)
    out.extend(po)

out.metadata = po.metadata
out.save(OUT)



# # determine total character size of all the entries in the file
# length = 0
# for index, entry in enumerate(po):
#     length += len(entry.msgid)

# print 'count %s, size %s' % (index + 1, length)

# # reopen as source for copying
# po = polib.pofile(FPATH)
# assert len(po)

# # build a list of endpoints for the slices
# ends = [0, len(po)]
# fraglen = 0
# for index, entry in enumerate(po):
#     fraglen += len(entry.msgid)
#     if fraglen >= length / FRAGS:
#         fraglen = 0
#         ends.insert(-1, index)

# # ouput the files
# for frag in range(FRAGS):
#     pp = list(os.path.splitext(FPATH))
#     pp.insert(1, '_%d' % frag)
#     start, end = ends[frag:frag + 2]
#     poslice = polib.POFile()
#     poslice.metadata = po.metadata
#     poslice.extend(po[start:end])
#     poslice.save(''.join(pp))

# print 'check the local directory for the split files.'
