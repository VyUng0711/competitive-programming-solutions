# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution:   
    def __init__(self):
        self.map_num_to_letter = {
            "0": "_",
            "1": None,
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
    

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        results = []
        
        def recurse(rest_of_the_word, path_so_far):
            
            if not rest_of_the_word:
                results.append(path_so_far)
                return 
            first, remaining = rest_of_the_word[0], rest_of_the_word[1:]
            letters = self.map_num_to_letter[first]
            
            for letter in letters:
                recurse(remaining, path_so_far + letter)
                
        recurse(digits, "")
        return results
        
