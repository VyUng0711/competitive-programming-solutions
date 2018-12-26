# https://www.spoj.com/problems/PERIOD/

num_test = int(input())
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
  
  
for t in range(num_test):
  print("Test case #{}".format(t + 1))
  n = int(input())
  s = input()
  kmp = [None] * n
  kmp_preprocess(s, kmp)
  # print(kmp)
  for i in range(0, n):
    lps = kmp[i]
    if lps != 0 and (i + 1) % (i + 1 - lps) == 0:
      print(i + 1, (i + 1) // (i + 1 - lps))
  if t != num_test - 1:
    print()


