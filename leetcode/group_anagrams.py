from collections import defaultdict
class Solution:
    # GROUP BY SORTED: O(n*k*logk)
    def groupAnagrams(self, strs):
        mapping = defaultdict(list)
        for word in strs:
            sorted_word = sorted(word)
            sorted_word = ''.join(sorted_word)
            mapping[sorted_word].append(word)
        return [x for x in mapping.values()]

    # GROUP BY COUNT O(n*k)
    def groupAnagrams(self, strs):
        mapping = defaultdict(list)
        for word in strs:
            count = [0]*26
            for letter in word:
                index = ord(letter) - ord('a')
                count[index] += 1
            mapping[tuple(count)].append(word)
        return [x for x in mapping.values()]
            
