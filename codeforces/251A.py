def points_on_line(l,d):
  j=0
  combination=0
  for i in range(len(l)):
    while j<len(l) and l[j]<=l[i]+d:
      j+=1
    nums=j-i-1
    combination+=nums*(nums-1)//2
  return combination

n,d=[int(x) for x in input().split()]
l=[int(x) for x in input().split()]
print (points_on_line(l,d))