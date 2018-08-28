# http://codeforces.com/problemset/problem/551/A
def gukiz_contest(l):
  a=l[:]
  a=sorted(a)
  a+=[10000]
  dict={}
  for i in range(len(a)-2,-1,-1):
    if a[i]!=a[i+1]:
      dict[a[i]]=1+(len(a)-2)-i
  ranks=[]
  for j in range(len(l)):
    ranks.append(dict[l[j]])
  print (*ranks)

n=int(input())
l=list(map(int, input().split()))
gukiz_contest(l)