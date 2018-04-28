def swapsort(n,a):
  swaps=[]
  s=sorted(a)
  for i in range(len(a)):
    if a[i] != s[i]:
      for j in range(i+1,len(a)):
        if a[j]==s[i]:
          a[i],a[j]=a[j],a[i]
          swaps.append([i,j])
          break
  print (len(swaps))
  for k in range(len(swaps)):
    print (*swaps[k])
n=int(input())
a=[int(x) for x in input().split()]
swapsort(n,a)