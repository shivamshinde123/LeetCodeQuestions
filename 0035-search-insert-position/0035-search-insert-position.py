class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        left_index, right_index = 0, n - 1
        
        while left_index <= right_index:
            
            mid_index = left_index + (right_index - left_index) // 2
            mid_value = nums[mid_index]
            
            if mid_value == target:
                return mid_index
            elif mid_value < target:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1
                
        
        return right_index + 1