class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        # creating two variables- one for tracking index and one for tracking length
        i = n - 1
        length = 0

        while s[i] == " ":
            i -= 1

        while s[i] != " " and i >= 0:
            i -= 1
            length += 1
        
        return length


            

