class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        freq = dict()
        result = list()

        for i in range(n):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            
            else:
                freq[nums[i]] += 1

        print(freq)

        for item, value in freq.items():
            if value > n // 3:
                result.append(item)

        return result