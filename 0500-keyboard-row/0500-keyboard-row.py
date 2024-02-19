class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        
        answer = []
        for word in words:
            if all(char in first_row for char in word.lower()) or all(char in second_row for char in word.lower()) or all(char in third_row for char in word.lower()):
                answer.append(word)
                
        return answer