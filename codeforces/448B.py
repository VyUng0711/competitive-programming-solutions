# http://codeforces.com/problemset/problem/448/B
def suffix_structure(s,t):
  j = 0
  for i in range(len(s)):
    if j == len(t):
      break
    if s[i]==t[j]:
      j+=1
  if j== len(t):
    result="automaton"
  else:
    sorted_s=sorted(s)
    sorted_t=sorted(t)
    if sorted_s==sorted_t:
      result="array"
    else:
      k=0
      for i in range(len(sorted_s)):
        if k == len(sorted_t):
          break
        if sorted_s[i]==sorted_t[k]:
          k+=1
      if k==len(sorted_t):
        result="both"
      else:
        result="need tree"
  return (result)
s=input()
t=input()
print (suffix_structure(s,t))