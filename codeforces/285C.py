# http://codeforces.com/problemset/problem/285/C
def build_permutation(l):
  s=sorted(l)
  p=[]
  for i in range(1,len(l)+1):
    p.append(i)
  sum=0
  for j in range(len(l)):
    if s[j]>=p[j]:
      sum+=s[j]-p[j]
    else:
      sum+=p[j]-s[j]
  print(sum)
n=int(input())
l=[int(x) for x in input().split()]
build_permutation(l)