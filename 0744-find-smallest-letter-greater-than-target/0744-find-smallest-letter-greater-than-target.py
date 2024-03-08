class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        n = len(letters)
        left_index, right_index = 0 , n - 1
        
        if target < letters[left_index] or target >= letters[right_index]:
            return letters[left_index]
        
        while left_index <= right_index:
            
            mid_index = left_index + (right_index - left_index) // 2
            mid_value = letters[mid_index]
            
            if mid_value <= target:
                left_index = mid_index + 1
            if mid_value > target:
                right_index = mid_index - 1
                
        return letters[left_index]
    