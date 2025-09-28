class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0

        if nums[0] < nums[-1]: # Array not rotated or has a drop at boundry
            count += 1

        # Count the number of drops (You will get one if largest values is in between smaller values)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                count += 1
            if count > 1:
                return False

        return True