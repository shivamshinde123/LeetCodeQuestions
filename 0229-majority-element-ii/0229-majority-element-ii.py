class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        req_freq = math.floor(len(nums)/3)
        
        freq = Counter(nums)
        answer = list()
        
        for key, value in freq.items():
            if value > req_freq:
                answer.append(key)
                
        return answer