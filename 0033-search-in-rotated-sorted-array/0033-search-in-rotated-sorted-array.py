class Solution:
    def search(self, nums: List[int], target: int) -> int:

        min_element_index = nums.index(min(nums))

        # if the array has length of one, then we won't need to use binary search
        if len(nums) == 1:
            if target in nums:
                return 0
            else:
                return -1

        if nums.index(min(nums)) ==  0: # If the array isn't rotated
            return self.bsearch(nums, target)
        else: # If the array is rotated
            if target >= nums[0]:
                return self.bsearch(nums[0:min_element_index], target)
            else:
                output = self.bsearch(nums[min_element_index:], target)
                if output != -1:
                    return output + min_element_index
                else:
                    return output

    
    def bsearch(self, nums, target):
        left_index = 0
        right_index = len(nums) - 1

        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            middle_value = nums[middle_index]

            if middle_value == target:
                return middle_index
            
            if middle_value < target:
                left_index = middle_index + 1
            else:
                right_index = middle_index - 1
        
        return -1
                

     
