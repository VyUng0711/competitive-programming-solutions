def transform_RPN(exp):
  stack=[]
  result=[]
  priority={'+':0,'-':1,'*':2,'/':3,'^':4}
  for i in range(len(exp)):
    if exp[i] not in ['+','-','*','/','^','(',')']:
      result.append(exp[i])
    elif exp[i]=='(':
      stack.append(exp[i])
    elif exp[i]==')':
      while len(stack)!=0 and stack[-1]!='(':
        result.append(stack[-1])
        stack.pop()
      stack.pop()
    elif exp[i] in ['+','-','*','/','^']:
      while stack[-1]!='('and len(stack)!=0 and priority[stack[-1]]>=priority[exp[i]]:
        result.append(stack[-1])
        stack.pop()
      stack.append(exp[i])
  for j in range(len(stack)-1,-1,-1):
    result.append(stack[j])
  result=''.join(result)
  return (result)
t = int(input())
list_of_str = []
for i in range(t):
  list_of_str.append(input())
for str in list_of_str:
  print (transform_RPN(str))