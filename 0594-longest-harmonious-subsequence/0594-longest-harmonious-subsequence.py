class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        num_freq = dict()
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        keys = num_freq.keys()
        max_len = 0
        for key in keys:
            if key + 1 in keys:
                max_len = max(max_len, num_freq[key] + num_freq[key + 1])

        return max_len


