class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        nums.sort()
        diff_to_sums = {}
        
        for i in range(n-1):
            
            j = i + 1
            k = n - 1
            
            while (j < k):
                sum_ = nums[i] + nums[j] + nums[k]
                    
                if sum_ < target:
                    j += 1
                elif sum_ > target:
                    k -= 1
                else:
                    j += 1
                    
                diff = abs(sum_ - target)
                diff_to_sums[diff] = sum_
                
            
            
                    
        return diff_to_sums[min(diff_to_sums.keys())]

                    