class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        # Approach 1: O(words * brokenLetters)
#         words = text.split()
#         true_count = 0
#         for word in words:
#             if all(letter not in word for letter in brokenLetters):
#                 true_count +=1
            
#         return true_count
    
        # Approach 2
        words = text.split()
        num_of_words = len(words)
        
        for word in words:
            for char in word:
                if char in brokenLetters:
                    num_of_words -= 1
                    break
                    
        return num_of_words
        