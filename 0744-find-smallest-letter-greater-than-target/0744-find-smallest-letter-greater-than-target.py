class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
#         n = len(letters)
#         left_index, right_index = 0 , n - 1
        
#         if target <= letters[left_index] or target >= letters[right_index]:
#             return letters[left_index]
        
#         while left_index <= right_index:
            
#             mid_index = left_index + (right_index - left_index) // 2
#             mid_value = letters[mid_index]
            
#             if mid_value <= target:
#                 left_index = mid_index + 1
#             elif mid_value > target:
#                 right_index = mid_index - 1
                
#         return letters[left_index]
    
        letters_length = len(letters)
        low = 0
        high = letters_length - 1
        
        if target < letters[low] or target >= letters[high]:
            return letters[low]

        while low <= high:
            middle =  (low + high) // 2
            candidate = letters[middle]
            
            if target < candidate: 
                high = middle - 1

            if target >= candidate :
                low = middle + 1
        
        return letters[low]