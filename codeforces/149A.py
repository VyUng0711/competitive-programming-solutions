def business_trip(k,l):
  s=sorted(l)
  total=0
  num=0
  for i in range(len(s)-1,-1,-1):
    if k==0:
      num=0
      break
    total+=s[i]
    num+=1
    #print(total)
    if total>=k:
      break
  if total<k:
    print (-1)
  else:
    print (num)
  
k=int(input())
l=list(map(int, input().split()))
business_trip(k,l)