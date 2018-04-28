def summer_sell_off(n,f,l):
  total=0
  a=[0]*n
  for i in range(n):
    total+=min(l[i][0],l[i][1])
    if l[i][0]<l[i][1]:
      a[i]=min(2*l[i][0],l[i][1])-min(l[i][0],l[i][1])
  s=sorted(a,reverse=True)
  j=0
  while f and j<n:
    if s[j]>0:
      total+=s[j]
      f-=1
    j+=1
  print (total)

n,f=[int(x) for x in input().split()]
l=[]
for i in range(n):
  l.append([int(x) for x in input().split()])
summer_sell_off(n,f,l)