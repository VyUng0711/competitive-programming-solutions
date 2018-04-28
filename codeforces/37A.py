def towers_2(n,l):
  sorted_l=sorted(l)
  sorted_l=sorted_l+[10000]
  values=[]
  keys=[]
  this_count=1
  for i in range(len(sorted_l)-1):
    if sorted_l[i+1]==sorted_l[i]:
      this_count+=1
    else:
      values.append(this_count)
      keys.append(sorted_l[i])
      this_count=1
  print (max(values),len(values))
n=int(input())
l=list(map(int, input().split()))
towers_2(n,l) 