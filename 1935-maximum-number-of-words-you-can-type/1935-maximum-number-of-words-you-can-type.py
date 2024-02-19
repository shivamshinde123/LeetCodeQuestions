class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        words = text.split()
        bools = list()
        for word in words:
            bools.append(all(letter not in word for letter in brokenLetters))
            
        return sum(1 for x in bools if x)