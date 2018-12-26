#https://leetcode.com/problems/find-duplicate-file-in-system/

from collections import defaultdict
class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        mapping = defaultdict(list)
        for p in paths:
            all_files = list(p.split())
            d = all_files[0]
            for file in all_files[1:]:
                name, content = file.split('(')
                content = content.split(')')[0]
                
                this_path = d + '/' + name
                mapping[content].append(this_path)
        return [x for x in mapping.values() if len(x) > 1]
        
               


