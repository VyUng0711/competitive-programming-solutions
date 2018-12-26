# https://www.codechef.com/problems/AUSAG

def kmp_preprocess(s, kmp):
  kmp[0] = 0
  i = 1
  j = 0
  while i < len(s):
    if s[i] == s[j]:
      j += 1
      kmp[i] = j
      i += 1
    else:
      if j != 0:
        j = kmp[j - 1]
      else:
        kmp[i] = 0
        i += 1

def kmp_search(t, p, kmp):
  count = 0 
  i = 0
  j = 0
  while i < len(t):
    if p[j] == t[i]:
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



num_test = int(input())
for t in range(num_test):
  S = input().replace(' ','')
  # print(S)
  s = input().replace(' ','')
  kmp = [None] * len(s)
  kmp_preprocess(s, kmp)
  res = kmp_search(S, s, kmp)
  print("Case {}: {}".format(t + 1, res))



