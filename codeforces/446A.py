def fast_dzy_loves_sequence(a):
  a=[10**9]+a+[0]
  lens=[]
  left=[]
  right=[]
  c_left=0
  c_right=0
  for i in range(0,len(a)):
    if i > 0 and a[i-1]<a[i]:
      c_left+=1
    else:
      c_left=1
    left.append(c_left)
  for j in range(len(a)-1,-1,-1):
    if j < len(a)-1 and a[j+1]>a[j]:
      c_right+=1
    else:
      c_right=1
    right.append(c_right)
  right.reverse()
  left[0]=0
  left[-1]=0
  right[0]=0
  right[-1]=0
  for k in range(1,len(a)-1):
    if a[k-1]+1 < a[k+1]:
      this_len=left[k-1]+1+right[k+1]
    else:
      this_len=max(left[k-1]+1,right[k+1]+1)
    lens.append(this_len) 
  return max(lens)
n=int(input())
a=[int(x) for x in input().split()]
print (fast_dzy_loves_sequence(a))