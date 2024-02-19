class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        ## Approach 1
#         first_row = "qwertyuiop"
#         second_row = "asdfghjkl"
#         third_row = "zxcvbnm"
#         answer = []
#         for word in words:
#             if all(char in first_row for char in word.lower()) or all(char in second_row for char in word.lower()) or all(char in third_row for char in word.lower()):
#                 answer.append(word)
                
#         return answer

        # Approach 2
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")
        answer = []
        for word in words:
            w = set(word.lower())
            
            if w.issubset(first_row) or w.issubset(second_row) or w.issubset(third_row):
                answer.append(word)
                
        return answer
            