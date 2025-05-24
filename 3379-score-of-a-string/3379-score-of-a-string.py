class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s)-1):
            curr = int(ord(s[i]))
            next = int(ord(s[i+1]))
            score += abs(curr - next)
            
        return score