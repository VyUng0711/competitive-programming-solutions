# https://leetcode.com/problems/integer-to-english-words/description/

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        teen_map = {'10':'Ten','11':'Eleven','12':'Twelve','13':'Thirteen','14':'Fourteen','15':'Fifteen','16':'Sixteen','17':'Seventeen','18':'Eighteen','19':'Nineteen'}
        ty_map = {'2':'Twenty','3':'Thirty','4':'Forty','5':'Fifty','6':'Sixty','7':'Seventy','8':'Eighty','9':'Ninety'}
        unit_map = {'0':'','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
        
        def helper(num):
            if num == '000':
                return ''
            if num[:2] == '00':
                return unit_map[num[-1]]
            
            last_two = num[1:]
            
            if last_two[0] == '1':
                last_two = teen_map[last_two]
                
            elif last_two[0] == '0':
                if last_two[1] == '0':
                    last_two = ''
                else:
                    last_two = unit_map[last_two[1]]
                    
            else:
                last_two = ty_map[last_two[0]] + ' ' + unit_map[last_two[1]]
                
            if num[0] == '0':
                return last_two
            
            return unit_map[num[0]] + ' Hundred ' + last_two
        
        num = str(num)
        
        num = '0' * (12-len(num)) + num
        print(num)
        high_level = [' Billion ',' Million ',' Thousand ',' ']
        result = ''        
        for i in range(4):
            tmp = helper(num[3 * i : 3 * i + 3])
            if tmp:
                result += (tmp + high_level[i])
            print(result)
        if not result:
            return 'Zero'
        return ' '.join(result.split())  
        
