# https://leetcode.com/problems/hamming-distance/description/

class Solution:
    def hammingDistance(self, x, y):

        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]
        if len(x_bin) < len(y_bin):
            x_bin = "0" * (len(y_bin) - len(x_bin)) + x_bin
        else:
            y_bin = "0" * (len(x_bin) - len(y_bin)) + y_bin
        # print(x_bin)
        # print(y_bin)
        count = 0
        for i in range(len(x_bin)):
            if x_bin[i] != y_bin[i]:
                count += 1
        return count
# SOLUTION USING XOR OPERATOR:
class Solution:
    def hammingDistance(self, x, y):

        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # print(bin(x))
        # print(bin(y))
        print(bin(x^y))
        return (bin(x^y)).count('1')
