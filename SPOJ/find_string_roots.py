# https://www.spoj.com/problems/FINDSR/


'''
A 
if the length of prefix = suffix is l
the length of the remaining is n - l
Because the remaining is part of the suffix, we have it equal
to the last part of the prefix with len n - l 

we have: 
A[n - l : l] = A[n - 2l: n - l]
similarly:
A[n - 2l: n - l] = A[n - 3l: n - 2l]
A[n - 3l: n - 2l] = A[n - 4l: n - 3l]
...
A[n - kl: n - (k- 1)l] = A[n - (k + 1)l: n - kl]
Therefore if n = kl (n % l == 0), 
we can find a k such that it splits the original strings
into equal substrings

abcabcabcabc
9 3
A[6:9] = A[9:12]
A[3:6] = A[6: 9]
K = 4


'''

def get_n(s):
  for l in range(1, len(s) // 2 + 1): # O(sqrt(N)), N = len(s)
    if len(s) % l == 0:
      n = len(s) // l
      if s[:l] * n == s:
        return n
  return 1

def get_n_kmp(s, kmp):
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

  lps = kmp[-1]
  # print(kmp)
  if len(s) % (len(s) - lps) == 0:
    return (len(s) // (len(s) - lps))
  return 1



while True:
  s = input()
  if s == "*":
    break

  kmp = [None] * len(s)
  res = get_n_kmp(s, kmp)
  print(res)

