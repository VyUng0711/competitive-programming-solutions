def sort_queries(a,b):
  a=sorted(a)
  c = b[:]
  c=sorted(c)
  i=0
  counts=[]
  dict = {}
  for j in range(len(c)):
    while i<len(a) and a[i]<=c[j]:
      i+=1
    dict[c[j]]=i
  for k in b:
    print (dict[k], end=' ')

n,m=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
sort_queries(a,b)