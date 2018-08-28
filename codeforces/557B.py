# http://codeforces.com/problemset/problem/557/B
def pasha_and_tea(n,w,l):
  s=sorted(l)
  if s[n]>=s[0]*2:
    girl=s[0]
    boy=s[0]*2
  else:
    girl=s[n]/2
    boy=s[n]
  if (girl+boy)*n<=w:
    print((girl+boy)*n)
  else:
    print(w)
n,w=list(map(int, input().split()))
l=list(map(int, input().split()))
pasha_and_tea(n,w,l)