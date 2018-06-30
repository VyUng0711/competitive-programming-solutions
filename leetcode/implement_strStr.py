# Solution with string slicing:
def strStr(self, haystack, needle):
    if needle == "":
        return 0
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack)):
        if haystack[i: i+len(needle)] == needle:
            return i 
    return -1

# Solution with no string slicing:
def strStr(self, haystack, needle):
    if needle == "":
        return 0
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            j = i + 1
            k = 1
            while j < len(haystack) and k < len(needle):
                if haystack[j] == needle[k] and k == len(needle) - 1: 
                    return (i)
                if haystack[j] != needle[k]:
                    break
                else:
                    j += 1
                    k += 1 
            if k == len(needle):
                return i      
    return -1
                    
        
        