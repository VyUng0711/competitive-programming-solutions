def braces( A):
  ops = '+-*/'
  stack = []
  for a in A:
    if a in ops or a == '(':
      stack.append(a)
    elif a == ')':
      if stack[-1] == '(':
        return 1
      while stack[-1] in ops:
        stack.pop()
      stack.pop()

  for val in stack:
    if val == "(" or val == ")":
      return 1
  return 0

print(braces('((a + b))'))
print(braces('(a + (a + b))'))
  
class Solution:
    # @param A : string
    # @return an integer
    def braces(self, s):
        last_pair = (-1, -1)
        st = []
        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            elif s[i] == ')':
                if last_pair == (st[-1] + 1, i - 1):
                    return 1
                last_pair = (st.pop(), i)
            else:
                last_pair = (i, i)
        return 0


