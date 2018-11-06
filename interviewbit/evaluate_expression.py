class Solution:
    def evalRPN(self, A):
        stack = []
        ops = "+-*/"
        for a in A:
            if a not in ops:
                stack.append(a)
            else:
                first = stack.pop()
                second = stack.pop()
                result = eval(second+a+first)
                stack.append(str(result))
        return int(float(stack[0]))

