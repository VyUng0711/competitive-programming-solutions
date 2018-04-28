def mmass(m):
  mass = {'C':12, 'O':16, 'H':1}
  stack = []
  for i in range(len(m)):
    if m[i] in ['C','O','H']:
      stack.append(mass[m[i]])
    elif m[i] == '(':
      stack.append(0)
    elif m[i] == ')':
      v = 0
      while len(stack)!=0 and stack[-1]!=0:
        v+=stack[-1]
        stack.pop()
      stack.pop()
      stack.append(v)
    else:
      v = stack[-1]
      stack.pop()
      stack.append(v * int(m[i]))
#     print (stack)
  total=0
  while len(stack)!=0:
    total+=stack[-1]
    stack.pop()
  print (total)
 
str=input().strip()
mmass(str)