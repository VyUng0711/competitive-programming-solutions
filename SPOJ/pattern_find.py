# https://www.spoj.com/problems/NAJPF/

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

# def kmp_pre(p):
#   kmp[0] = -1
#   j = -1
#   for i in range(1, len(p)):
#     while j > -1 and p[j + 1] != p[i]:
#       j += 1
#     if p[j + 1] == p[i]:
#       j += 1
#     kmp[i] = j



def kmp_search(t, p, kmp):
  i = 0
  j = 0
  found_inds = []
  while i < len(t):
    if p[j] == t[i]:
      i += 1
      j += 1
      if j == len(p):
        found_inds.append(i - j)
        j = kmp[j - 1]
    else:
      if j != 0:
        j = kmp[j - 1]
      else:
        i += 1
  return found_inds


t = int(input())
for i in range(t):
  A, B = input().split()
  kmp = [None] * len(B)
  kmp_preprocess(B, kmp)
  res = kmp_search(A, B, kmp)
  if res:
    print(len(res))
    for i in res:
      print(i + 1, end=' ')
    print()
  else:
    print("Not Found")
  print()


