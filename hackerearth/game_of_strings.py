# https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/game-of-strings-2/description/

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
 
t = int(input())
for i in range(t):
  s, k = input().split()
  k = int(k) - 1
  kmp = [None] * len(s)
  # O(len(S))
  kmp_preprocess(s, kmp)

  max_len = max(kmp[: k + 1])
 
  res = None
  j = kmp[-1]
  # O(len(S)) 
  while j > 0:
    if j <= max_len:
      res = j
      break
    j = kmp[j - 1]
    # for i in range(0, k + 1):
    #   if kmp[i] == j:
    #     res = j
    #     break
    # if res != -1:
    #   break
    
 
  if not res:
    print("Puchi is a cheat!")
  else:
    print(s[:res])
