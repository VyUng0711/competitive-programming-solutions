# http://codeforces.com/problemset/problem/372/A
def kangaroo(l):
  l=sorted(l)
  i=0
  j=len(l)//2
  count=0
  while j<len(l) and i<len(l)//2:
    if l[j]>=2*l[i]:
      count+=1
      i+=1
    j+=1
  return (len(l)-count)
s = []
n = int(input())
for i in range(n):
  s.append(int(input()))
print (kangaroo(s))