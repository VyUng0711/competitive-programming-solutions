def sort_the_array(n,a):
  s = sorted(a)
  left = 0
  for i in range(len(a)-1):
    if a[i]>a[i+1]:
      left=i
      break
  right=left
  while right<n-1 and a[right]>a[right+1]:
    right+=1
  a[left:right+1]=reversed(a[left:right+1])
  #print (a)
  if a == s:
    print ("yes")
    print (left+1,right+1) 
  else:
    print ("no")
n=int(input())
a=list(map(int, input().split()))
sort_the_array(n,a)