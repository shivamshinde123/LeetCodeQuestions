class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        return self.bsearch(nums, target)
        

    def bsearch(self, nums, target):
        left_index = 0
        right_index = len(nums) - 1
        middle_index = 0

        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            left_value = nums[left_index]
            right_value = nums[right_index]
            middle_value = nums[middle_index]

            if target == middle_value:
                return True

            # If we could not find in which part does the middle value lies
            if middle_value == right_value: 
                right_index -= 1
            # If middle value is in the left sorted part of array
            elif middle_value > right_value: 
                if left_value <= target and target < middle_value:
                    right_index = middle_index - 1
                else:
                    left_index = middle_index + 1
            # If middle valie is in the right sorted part of array
            else:
                if right_value >= target and target > middle_value:
                    left_index = middle_index + 1
                else:
                    right_index = middle_index - 1     

        return False
