class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Brute force solution - O(N^3) - Time Limit Exceeded
        # ans = list()
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1, n):
        #             if nums[i] + nums[j] + nums[k] == 0 and sorted([nums[i], nums[j], nums[k]]) not in ans:
        #                 ans.append(sorted([nums[i], nums[j], nums[k]]))

        # return ans

        # 3 pointer approach
        n = len(nums)
        nums.sort()
        ans = list()
        for i in range(n):

            # remove duplicates
            if i != 0 and nums[i] == nums[i-1]:
                    continue 

            left = i + 1
            right = n - 1

            while left < right:

                total_sum = nums[i] + nums[left] + nums[right]
                
                if total_sum < 0:
                    left += 1
                
                elif total_sum > 0:
                    right -= 1

                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skipping the duplicate values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and  nums[right] == nums[right + 1]:
                        right -= 1

        return ans