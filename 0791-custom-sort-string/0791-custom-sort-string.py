class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        freq = dict()
        
        for char in s:
            freq[char] = freq.get(char, 0) + 1
            
        answer = ""
        
        for char in order:
            if char in s:
                answer += char*freq[char]
                del freq[char]
        
        # Python 3.6 onwards, python dictionaries are ordered. That means items will be in order of their addition into the dict.
        for char, count in freq.items():
            answer += char*count
        
        return answer
        
        