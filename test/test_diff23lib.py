#!/usr/bin/python3
# vim:se tw=79 sts=4 ts=4 et ai:
"""
Console script to test diff2lib and diff3lib used by imediff

Current diff2 uses Python standard library difflib which uses a variant of
longest contiguous matching subsequence algorithm by Ratcliff and Obershelp
developed in the late 1980's.  If I update this imediff program to use more
modern algorithm, this test may yield slightly different result.
"""
import sys
sys.path.insert(0, '..')
import imediff.diff2lib
import imediff.diff3lib

print('===========================================================')
a = "pqabxcdsdgpx"
b = "zabycdfsdgpx"
c = "zabycdfzcpgpx12345"
print("a='%s' -> %i" % (a, len(a)))
print("b='%s' -> %i" % (b, len(b)))
print("c='%s' -> %i" % (c, len(c)))
sa = imediff.diff2lib.SequenceMatcher2(None, a, b)
print("--- BA ---")
for tag, i1, i2, j1, j2 in sa.get_chunks():
   print(("%2s     a[%d:%d] (%s) / b[%d:%d] (%s)" %
          (tag, i1, i2, a[i1:i2], j1, j2, b[j1:j2])))
print("--- BC ---")
sc = imediff.diff2lib.SequenceMatcher2(None, c, b)
for tag, i1, i2, j1, j2 in sc.get_chunks():
   print(("%2s     c[%d:%d] (%s) / b[%d:%d] (%s)" %
          (tag, i1, i2, c[i1:i2], j1, j2, b[j1:j2])))
s = imediff.diff3lib.SequenceMatcher3(None, a, b, c)
print("--- ABC ---")
for tag, i1, i2, j1, j2, k1, k2 in s.get_chunks():
   print(("%2s     a[%d:%d] (%s) / b[%d:%d] (%s) / c[%d:%d] (%s)" %
          (tag, i1, i2, a[i1:i2], j1, j2, b[j1:j2], k1, k2, c[k1:k2])))
print('===========================================================')
a = "asxxdfghjkl"
b = "asdffghjl"
c = "sxxdfghjk"
print("a='%s' -> %i" % (a, len(a)))
print("b='%s' -> %i" % (b, len(b)))
print("c='%s' -> %i" % (c, len(c)))
sa = imediff.diff2lib.SequenceMatcher2(None, a, b)
print("--- BA ---")
for tag, i1, i2, j1, j2 in sa.get_chunks():
   print(("%2s     a[%d:%d] (%s) / b[%d:%d] (%s)" %
          (tag, i1, i2, a[i1:i2], j1, j2, b[j1:j2])))
print("--- BC ---")
sc = imediff.diff2lib.SequenceMatcher2(None, c, b)
for tag, i1, i2, j1, j2 in sc.get_chunks():
   print(("%2s     c[%d:%d] (%s) / b[%d:%d] (%s)" %
          (tag, i1, i2, c[i1:i2], j1, j2, b[j1:j2])))
s = imediff.diff3lib.SequenceMatcher3(None, a, b, c)
print("--- ABC ---")
for tag, i1, i2, j1, j2, k1, k2 in s.get_chunks():
   print(("%2s     a[%d:%d] (%s) / b[%d:%d] (%s) / c[%d:%d] (%s)" %
          (tag, i1, i2, a[i1:i2], j1, j2, b[j1:j2], k1, k2, c[k1:k2])))
print('===========================================================')
a = "AFFSDCFiasVXGBAZDFhhVaaGB"
b = "ASDCFVXGnBAZDFVGfgBAZDB"
c = "AFFSCFiasVXGfBAZDFhhVGB"
print("a='%s' -> %i" % (a, len(a)))
print("b='%s' -> %i" % (b, len(b)))
print("c='%s' -> %i" % (c, len(c)))
sa = imediff.diff2lib.SequenceMatcher2(None, a, b)
print("--- BA ---")
for tag, i1, i2, j1, j2 in sa.get_chunks():
   print(("%2s     a[%d:%d] (%s) / b[%d:%d] (%s)" %
          (tag, i1, i2, a[i1:i2], j1, j2, b[j1:j2])))
print("--- BC ---")
sc = imediff.diff2lib.SequenceMatcher2(None, c, b)
for tag, i1, i2, j1, j2 in sc.get_chunks():
   print(("%2s     c[%d:%d] (%s) / b[%d:%d] (%s)" %
          (tag, i1, i2, c[i1:i2], j1, j2, b[j1:j2])))
s = imediff.diff3lib.SequenceMatcher3(None, a, b, c)
print("--- ABC ---")
for tag, i1, i2, j1, j2, k1, k2 in s.get_chunks():
   print(("%2s     a[%d:%d] (%s) / b[%d:%d] (%s) / c[%d:%d] (%s)" %
          (tag, i1, i2, a[i1:i2], j1, j2, b[j1:j2], k1, k2, c[k1:k2])))