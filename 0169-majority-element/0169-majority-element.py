class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ## Insertion sort
        for i in range(1, len(nums)):
            anchor = nums[i]
            j = i - 1
            while j >= 0 and anchor < nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            
            nums[j+1] = anchor
        
        ## After sorting, majority element (elements that repeats itself atleast n//2+1 times)
        ## lies at n//2 th place
        return nums[math.floor(len(nums)/2)]