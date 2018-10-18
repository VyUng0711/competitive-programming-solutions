# https://leetcode.com/problems/longest-palindromic-substring/description/

# Method 1: Dynamic Programming:
class Solution(object):
    def longestPalindrome(self, s):
        dp = [[True] * len(s) for _ in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = True
            
        for i in range(len(s) - 1):
            if s[i + 1] == s[i]:
                dp[i][i + 1] = True
            else:
                dp[i][i + 1] = False
                
        max_len = 0
        max_i = 0
        max_j = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                    if dp[i][j] and j - i + 1 > max_len:
                        max_len = j - i + 1
                        max_i = i
                        max_j = j
                else:
                    dp[i][j] = False       
        return s[max_i: max_j + 1]

# Method 2: Expand from middle of string:
class Solution(object):
    def longestPalindrome(self, s):
        def expand(left, right, s):      
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right +=1
            return right - left - 1
        
        
        
        global_max = 0
        global_left = 0
        global_right = 0
        for i in range(len(s)):
            len_1 = expand(i, i, s)
            len_2 = expand(i, i + 1, s)
            max_len = max(len_1, len_2)
            
            if max_len > global_max:
                # print(max_len)
                global_max = max_len
                global_left = i - (max_len - 1) // 2
                global_right = i + max_len // 2
                
            # print(global_left, global_right)
        return s[global_left: global_right + 1]
            
