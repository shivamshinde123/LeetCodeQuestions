class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for element in nums:
            if element != val:
                nums[j] = element
                j += 1
        return j