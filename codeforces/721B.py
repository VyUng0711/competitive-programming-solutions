# http://codeforces.com/problemset/problem/721/B
def password(n,k,passwords, correct):
  lengths=[]
  
  less=0
  equal=0
  
  for i in range(n):
    this_len=len(passwords[i])
    lengths.append(this_len)
  for j in range(n):
    if lengths[j] < len(correct):
      less+=1 
    elif lengths[j] > len(correct):
      pass
    elif lengths[j] == len(correct):
      equal+=1 
  
  best_case=less+(less//k)*5+1
  worst_case=less+equal+((less+equal-1)//k)*5
  print(best_case,worst_case)
 

n,k=map(int,input().split())
passwords=[]
for i in range(n):
  passwords.append(input())
correct=input()
password(n,k,passwords,correct)