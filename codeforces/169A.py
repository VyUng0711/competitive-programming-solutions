def chores(n,a,b,h):
  h.sort()
  return (h[b]-h[b-1])
n,a,b=[int(x) for x in input().split()]
h = list(map(int, input().split()))
print (chores(n,a,b,h))