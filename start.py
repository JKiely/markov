import sys
from ngrams import Ngram

N = 2
f = "journal.txt"
l = 20

if len(sys.argv) > 1:
    N = int(sys.argv[1])

if len(sys.argv) > 2:
    f = str(sys.argv[2])

if len(sys.argv) > 3:
    l = int(sys.argv[3])

n = Ngram(f, n = N)

for _ in xrange(5):
    print n.make(length = l)
