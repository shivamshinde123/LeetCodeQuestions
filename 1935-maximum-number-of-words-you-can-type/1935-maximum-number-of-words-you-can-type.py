class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        words = text.split()
        true_count = 0
        for word in words:
            if all(letter not in word for letter in brokenLetters):
                true_count +=1
            
        return true_count