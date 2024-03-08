class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        freq = dict()
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
        max_freq = max(freq.values())

        total_freq = 0

        for value in freq.values():
            if value == max_freq:
                total_freq += value
                
        return total_freq
                
        