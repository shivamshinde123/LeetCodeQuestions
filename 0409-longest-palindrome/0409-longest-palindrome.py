class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        count = dict()
        
        for char in s:
            count[char] = count.get(char,0) + 1
            
        even_val_sum = 0
        odd_val = list()
        
        for val in count.values():
            if val % 2 == 0:
                even_val_sum += val
            else:
                odd_val.append(val)
                
        longest_palin = even_val_sum
        
        odd_val.sort(reverse=True)
        
        if len(odd_val) == 1:
            longest_palin = longest_palin + odd_val[0]
        elif len(odd_val) > 1:
            longest_palin += odd_val[0] + sum(list(map(lambda x: x-1, odd_val[1:])))
        
        return longest_palin