def oath(l):
  s=sorted(l)
  result=0
  for i in l:
    if i > s[0] and i < s[-1]:
      result+=1
  print (result)
 
n=int(input())
l=[int(x) for x in input().split()]
oath(l)