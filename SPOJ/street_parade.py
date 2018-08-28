# https://www.spoj.com/problems/STPAR/

def street_parade(l):
  stack=[]
  new_line=[]
  index=1
  for truck in l:
    if truck!=index:
      if len(stack)!=0:
        for j in range(len(stack)):
          if stack[-1]==index:
            new_line.append(stack[-1])
            stack.pop()
            index+=1
          else:
            break
        if truck==index:
          new_line.append(truck)
          index+=1
        else:
          stack.append(truck)
      else:
        stack.append(truck)
    else:
      new_line.append(truck)
      index+=1
  #print(stack)
  for i in range(len(stack)):
    new_line.append(stack[-1])
    stack.pop()
  #print (new_line)
  if new_line == sorted(l):
    print ("yes")
  else:
    print ("no")
    
cont=True
while cont:
  n = int(input())
  if n == 0:
    cont=False
    break
  l = [int(x) for x in input().split()]
  street_parade(l)