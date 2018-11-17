# https://leetcode.com/problems/first-unique-character-in-a-string/description/

class Solution:
    def firstUniqChar(self, s):
        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
        print(d)
        for j in range(len(s)):
            if d[s[j]] == 1:
                return j
        return -1


def firstUniqChar(s):
    if s == "":
        return -1
    count_dict = {}
    for i in range(len(s)):
        if s[i] not in count_dict:
            count_dict[s[i]] = i
        else:
            count_dict[s[i]] = len(s)
    min_index = len(s)
    for key, value in count_dict.items():
        if value < min_index:
            min_index = value
    if min_index == len(s):
        return -1
    return min_index

#print (firstUniqChar("leetcode"))
