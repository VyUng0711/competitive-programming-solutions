# https://codeforces.com/gym/101466/problem/E
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
  
def kmp_search(s, t, pre_indx, kmp):
  i = 0
  j = 0
  count = 0
  while i < len(s):
    if s[i] == t[j]:
      i += 1
      j += 1
      if j == pre_indx:
        count += 1
        j = kmp[j - 1]
    else:
      if j != 0:
        j = kmp[j - 1]
      else:
        i += 1
  return count


A = input()
B = input()
n = int(input())
kmp = [None] * len(B)
kmp_preprocess(B, kmp)
# print(kmp)
# pre_indx = len(B)

# O(len(B) * len(A)) --> 10 ** 10
# occ(B[:pre_indx]) >= n
# -> occ(B[:less_pre_indx]) >= n

res = 0
high = len(B)
low = 0
while low <= high:
  mid = (low + high) // 2
  if kmp_search(A, B, mid, kmp) >= n:
    res = mid
    low = mid + 1
  else:
    high = mid - 1


# while pre_indx > 0:
#   res = kmp_search(A, B, pre_indx, kmp)
#   pre_indx -= 1
#   if res >= n:
#     break
  # print("pre_indx: {}, res: {} ".format(pre_indx, res))
  
if res > 0:
  # print(res)
  print(B[: res])
else:
  print("IMPOSSIBLE")




