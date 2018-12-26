# https://leetcode.com/problems/valid-anagram/

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # O(n log log n)
        is_prime = [True] * n
        
        i = 2
        while i * i < n:
            if is_prime[i]:
                j = i * i
                while j < n:
                    is_prime[j] = False
                    j += i
            i += 1
        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1
        return count
        
        
        # O(n ^ 1.5)
        # def isPrime(num):
        #     if num <= 1:
        #         return False
        #     i = 2
        #     while i * i <= num:
        #         if num % i == 0:
        #             return False
        #         i += 1
        #     return True
        # count = 0
        # for i in range(n):
        #     if isPrime(i):
        #         count += 1
        # return count


