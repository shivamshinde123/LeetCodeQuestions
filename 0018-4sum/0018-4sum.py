class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # Approach 1: Using threeSum method
#         n = len(nums)
#         output = list()
#         nums.sort()
        
#         def threeSum(nums, target):
#             answer = set()
#             n = len(nums)
            
#             for i in range(n-1):

#                 j = i + 1
#                 k = n - 1

#                 while j < k:
#                     sum_ = nums[i] + nums[j] + nums[k]

#                     if sum_ == target:
#                         answer.add((nums[i], nums[j], nums[k]))
#                         j += 1
#                     elif sum_ > target:
#                         k -= 1
#                     else:
#                         j += 1

#             return list(answer)
        
#         for i in range(n-2):
#             out = threeSum(nums[i+1:], target-nums[i])
            
#             for item in out:
#                 if [nums[i]] + list(item) not in output:
#                     output.append([nums[i]] + list(item))
        
#         return output
    
        # Approach 2: Intergrating threeSum into only one function
        n = len(nums)
        answer = set()
        nums.sort()
        
        for i in range(n-2):
            
            for j in range(i+1, n-1):
                k = j + 1
                l = n - 1
                
                while k < l:
                    sum_ = nums[i] + nums[j] + nums[k] + nums[l]
                    
                    if sum_ == target:
                        answer.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                    elif sum_ > target:
                        l -= 1
                    else:
                        k += 1
                        
        return list(answer)
                
                
            