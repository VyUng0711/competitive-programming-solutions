class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        split_A = A.split('/')
        # split_A = split_A[1:-1]
        stack = []
        for val in split_A:
            if val == '.' or val == '':
                continue
            elif val == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(val)
        result = "/"
        # print(stack)
        for i in range(len(stack)):
            result += stack[i]
            if i != len(stack) - 1:
                result += '/'
        return result


def simplifyPath(self, A):
  st = []
  A = [x for x in A.split('/') if x != '']
  for d in A:
      if d == '..':
          if st != []:
              st.pop()
      elif d != '.':
          st.append(d)
  return '/' + '/'.join(st)    
