class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        answer = set()
        n = len(nums)
        
        nums.sort()
        
        for i in range(n-1):
            
            j = i + 1
            k = n - 1
            
            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                
                if sum_ == 0:
                    answer.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif sum_ > 0:
                    k -= 1
                else:
                    j += 1
                
        return list(answer)
                
            
                    