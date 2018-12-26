# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1620

def kmp_preprocess(t, kmp):
  kmp[0] = 0
  i = 1
  j = 0
  while i < len(t):
    if t[i] == t[j]:
      j += 1
      kmp[i] = j
      i += 1
    else:
      if j != 0:
        j = kmp[j - 1]
      else:
        kmp[i] = 0
        i += 1

def kmp_search(s, t, kmp):
  i = 0
  j = 0
  while i < len(s):
    if s[i] == t[j]:
      i += 1
      j += 1
      if j == len(t):
        return True
    else:
      if j != 0:
        j = kmp[j - 1]
      else:
        i += 1
  return False

k = int(input())
for i in range(k):
  s = input()
  q = int(input())
  for j in range(q):
    t = input()
    kmp = [None] * len(t)
    kmp_preprocess(t, kmp)
    res = kmp_search(s, t, kmp)
    if res:
      print('y')
    else:
      print('n')





