# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4195

def kmp_preprocess(p, kmp):
  kmp[0] = 0
  i = 1
  j = 0
  while i < len(p):
    if p[i] == p[j]:
      j += 1
      kmp[i] = j
      i += 1
    else:
      if j != 0:
        j = kmp[j - 1]
      else:
        kmp[i] = 0
        i += 1 

def kmp_search(p, s, kmp):
  i = 0
  j = 0
  count = 0
  while i < len(s):
    if s[i] == p[j]:
      i += 1
      j += 1
      if j == len(p):
        count += 1
        j = kmp[j - 1]
    else:
      if j != 0:
        j = kmp[j - 1]
      else:
        i += 1
  return count

# O(t * n * len(s))

while True:
  n = int(input())
  if n == 0:
    break
  ps = []
  for i in range(n):
    ps.append(input())
  s = input()
  max_count = -1
  dominate = []
  for p in ps:
    kmp = [None] * len(p)
    kmp_preprocess(p, kmp)
    c = kmp_search(p, s, kmp)
    if c > max_count:
      dominate = [p]
      max_count = c
    elif c == max_count:
      dominate.append(p)
  print(max_count)
  for d in dominate:
    print(d)


