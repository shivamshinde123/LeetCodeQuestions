class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_s = [char for char in s.lower() if char.isalnum()]
        
        return clean_s == clean_s[::-1]

        