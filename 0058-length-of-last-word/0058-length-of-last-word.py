class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # Approach 1
        # return len(s.split()[-1])
        
        # Approach 2
        words = s.split()
        for i in range(len(words)-1,-1,-1):
            if words[i] != " ":
                return len(words[i])