# https://leetcode.com/problems/string-compression/

# Modify in-place:

class Solution:
    def compress(self, chars):
        read = 0
        write = 0
        cur_count = 1
        for read in range(len(chars)):
            if read + 1 == len(chars) or chars[read + 1] != chars[read]:
                chars[write] = chars[read]
                if cur_count > 1:
                    for i in range(len(str(cur_count))):
                        chars[write + 1 + i] = str(cur_count)[i]
                    write = write + 1 + len(str(cur_count))
                else:
                    write = write + 1
                cur_count = 1
            else:
                cur_count += 1
        return (write)


# Use extra space:

class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        res = []
        cur_count = 1
        for i in range(len(chars)):
            if i + 1 == len(chars) or chars[i + 1] != chars[i]:
                res.append(chars[i])
                if cur_count > 1:
                    for x in str(cur_count):
                        res.append(x)
                cur_count = 1
            else: 
                cur_count += 1
         
        for i in range(len(res)):
            chars[i] = res[i]
            
        return len(res)



