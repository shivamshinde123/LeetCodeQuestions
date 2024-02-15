class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Approach 1
        # unique_elements = list(set(nums))
        # return int((3*sum(unique_elements) - sum(nums))/2)

        # Appraoch 2
        d = dict()

        for num in nums:
            if num not in d.keys():
                d[num] = 1
            else:
                d[num] += 1
            
        for key in d.keys():
            if d[key] == 1:
                return key
        
