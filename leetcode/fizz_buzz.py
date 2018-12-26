# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
                

# More organized way to reduce the conditions: 

class Solution:
    def fizzBuzz(self, n):
        res = []
        for i in range(1, n + 1):
            to_str = ""
            if i % 3 == 0:
                to_str += "Fizz"
            if i % 5 == 0:
                to_str += "Buzz"
            if not to_str:
                to_str = str(i)
            res.append(to_str)
        return res


