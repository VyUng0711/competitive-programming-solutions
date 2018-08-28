# http://codeforces.com/problemset/problem/456/A
def laptops(l):
  sort_by_price=sorted(l,key=lambda x:x[0])
  quality=[x[1]for x in sort_by_price]
  sorted_quality=sorted([x[1] for x in l])
  if quality == sorted_quality:
    print("Poor Alex")
  else:
    print("Happy Alex") 
n=int(input())
l=[]
for i in range(n):
  l.append([int(x) for x in input().split()])
#l=[[1,2],[2,1]]      
laptops(l)