# http://codeforces.com/problemset/problem/439/B
def dumb_guy(x,l):
  a=sorted(l)
  total=0
  for i in range(len(a)):
    m = x-i
    if m < 1:
      m = 1
    total+=m*a[i]
  print (total)
  
n,x=list(map(int, input().split()))
l=list(map(int, input().split()))
dumb_guy(x,l)