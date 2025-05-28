class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        n = len(t)
        m = len(s)

        i = j = 0

        while i < n and j < m:
            print(f"i: {i} and j: {j}")
            if s[j] == t[i]:
                i += 1
                j += 1
            else:
                j += 1

        

        return n - i