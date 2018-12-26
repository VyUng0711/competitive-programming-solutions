# https://codeforces.com/problemset/problem/471/D

n, w = map(int, input().split())
bear = list(map(int, input().split()))
elephant = list(map(int, input().split()))

s = []
for i in range(len(bear) - 1):
  s.append(bear[i + 1] - bear[i])
p = []
for i in range(len(elephant) - 1):
  p.append(elephant[i + 1] - elephant[i])

# print(s)
# print(p)

kmp = [None] * len(p)
def kmp_preprocess(p, kmp):
  kmp[0] = 0
  j = 0
  i = 1
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
def kmp_search(s, p, kmp):
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

if len(elephant) > 1:
  kmp_preprocess(p, kmp)
  print(kmp_search(s, p, kmp))
else:
  print(len(bear))


