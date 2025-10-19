class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashmap = Counter(nums)
        n = len(nums)
        for item in hashmap:
            if hashmap[item] > (n // 2):
                return item