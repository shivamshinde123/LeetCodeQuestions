class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        output = list()
        nums.sort()
        
        def threeSum(nums, target):
            answer = set()
            n = len(nums)
            
            for i in range(n-1):

                j = i + 1
                k = n - 1

                while j < k:
                    sum_ = nums[i] + nums[j] + nums[k]

                    if sum_ == target:
                        answer.add((nums[i], nums[j], nums[k]))
                        j += 1
                    elif sum_ > target:
                        k -= 1
                    else:
                        j += 1

            return list(answer)
        
        for i in range(n-2):
            out = threeSum(nums[i+1:], target-nums[i])
            
            for item in out:
                if [nums[i]] + list(item) not in output:
                    output.append([nums[i]] + list(item))
            
                
        return output