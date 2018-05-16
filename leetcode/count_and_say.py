class Solution:
    def countAndSay(self, n):
        def next_number(current):
            next_number = ""
            count = 0
            i = 0
            while i < len(current):
                count = 1
                while i + 1 < len(current) and current[i] == current[i+1]:
                    i += 1
                    count += 1
                next_number += str(count)
                next_number += current[i]
                i+=1 
            return next_number
        start = '1'
        for i in range(1, n):
            start = next_number(start)
        return (start)
