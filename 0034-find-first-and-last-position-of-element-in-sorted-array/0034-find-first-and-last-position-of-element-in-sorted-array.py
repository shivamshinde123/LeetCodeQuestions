class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start_index = self.bsearch_findFirst(nums, target)
        end_index = self.bsearch_findLast(nums, target)
        return [start_index, end_index]
            
    def bsearch_findFirst(self, nums, target):

        left_index = 0
        right_index = len(nums) - 1
        middle_index = 0

        while left_index <= right_index:
            middle_index = (left_index + right_index)  // 2
            middle_value = nums[middle_index]

            if target == middle_value:
                ## THIS IF..ELSE PART IS IMPORTANT
                if middle_index == 0 or nums[middle_index - 1] != target:
                    return middle_index
                else:
                    right_index = middle_index - 1

            elif target < middle_value:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1

        return -1 

    def bsearch_findLast(self, nums, target):

        left_index = 0
        right_index = len(nums) - 1
        middle_index = 0

        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            middle_value = nums[middle_index]

            if target == middle_value:
                ## THIS IF..ELSE PART IS IMPORTANT
                if middle_index == len(nums) - 1 or nums[middle_index + 1] != target:
                    return middle_index
                else:
                    left_index = middle_index + 1
            elif target < middle_value:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1

        return -1 