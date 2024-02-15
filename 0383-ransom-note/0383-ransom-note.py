class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransom_freq = {elem: 0 for elem in set(magazine)}
        
        for char in ransomNote:
            ransom_freq[char] = ransom_freq.get(char, 0) + 1
            
        magazine_freq = {elem: 0 for elem in set(magazine)}
        
        for char in magazine:
            magazine_freq[char] = magazine_freq.get(char, 0) + 1
            
        for item in set(ransomNote):
            if (item not in magazine):
                return False
            elif (ransom_freq[item] > magazine_freq[item]):
                return False
            # We are writting if-elif statement here because if item is not in magazine then it won't have magazine_freq[item] and if we write both the conditions from if and elif together using or operator, we would get an error
        return True