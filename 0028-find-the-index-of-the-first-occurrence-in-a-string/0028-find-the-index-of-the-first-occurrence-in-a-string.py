class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) > len(haystack):
            return -1
        
        needle_length = len(needle)
        
        i = 0
        while i < len(haystack) - needle_length + 1:
            if haystack[i:i+needle_length] == needle:
                return i
            i += 1
            
        return -1