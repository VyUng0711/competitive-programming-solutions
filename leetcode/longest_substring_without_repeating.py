https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        max_len_so_far = 1
        last_occur = {s[0]: 0}
        j = 0
        for i in range(1, len(s)):
            if s[i] not in last_occur or last_occur[s[i]] < j:
                max_len_so_far = max(max_len_so_far, i - j + 1)
            else:
                j = last_occur[s[i]] + 1
            last_occur[s[i]] = i
            print(max_len_so_far)
                
        return max_len_so_far

