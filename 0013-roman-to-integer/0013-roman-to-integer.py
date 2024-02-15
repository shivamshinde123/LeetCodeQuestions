class Solution:
    def romanToInt(self, s: str) -> int:

        values = {
            'I': 1,
            'V': 5, 
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        int_value = 0
        i = 0
        while i < len(s):
            if (i < len(s) - 1) and values[s[i]] < values[s[i+1]]:
                int_value -= values[s[i]]
            else:
                int_value += values[s[i]]
            
            i += 1

        return int_value
