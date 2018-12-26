# http://codeforces.com/contest/126/problem/B

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

s = input()
kmp = [None] * len(s)
kmp_preprocess(s, kmp)

res = None
for i in range(len(s) - 1):
  if kmp[i] == kmp[-1]:
    res = kmp[-1]
    break

if not res:
  if kmp[kmp[-1] - 1] != 0:
    res = kmp[kmp[-1] - 1]

if not res:
  print("Just a legend") 
else:
  print(s[:res])
  

# abcabcabc --> abc is suffix

# abcdabc --> ab not suffix



# abcabcabc
# kmp i
# l = kmp[i] = kmp[-1]
# s[: l] prefix suffix
# s[:l] == s[i - l:i + 1] == s[-l:]

# l = kmp[kmp[-1] - 1]
# prefix suffix s[:l] = suffix s



#  a  a  a  a  a  a  a  a  a  a  a   a
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]






