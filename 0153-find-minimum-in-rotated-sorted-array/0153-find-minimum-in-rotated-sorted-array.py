class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left_index = 0
        right_index = len(nums) - 1
        
        # here we won't use "<=", cause that will make the while loop a infinite while loop 
        # because we don't have any return statement in this while loop
        while (left_index < right_index):

            middle_index = (left_index + right_index) // 2
            middle_value = nums[middle_index]
            right_value = nums[right_index]
            
            if middle_value <= right_value:
                ## In this case, middle value could be minimum value
                right_index = middle_index 
            else:
                # In this case, middle value has atleast one value smaller than it after it
                # So we can safely ignore the middle value and take the next one
                left_index = middle_index + 1

        return nums[left_index]