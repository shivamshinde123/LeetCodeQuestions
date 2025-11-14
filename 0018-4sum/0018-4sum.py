class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # # Using 2 pointer solution 
        # n = len(nums)
        # ans = list()
        # nums.sort() # sorting the array

        # # calculating the quadruplets
        # for i in range(n):
        #     # avoid duplicates while moving i
        #     if i != 0 and nums[i] == nums[i - 1]:
        #         continue

        #     for j in range(i+1, n):
        #         # avoid duplicates while moving j
        #         if j > i+ 1 and nums[j] == nums[j - 1]:
        #             continue

        #         # 2 pointer
        #         left = j + 1
        #         right = n - 1

        #         while left < right:

        #             total_sum = nums[i] + nums[j] + nums[left] + nums[right]

        #             if total_sum < target:
        #                 left += 1

        #             elif total_sum > target:
        #                 right -= 1

        #             else:
        #                 ans.append([nums[i], nums[j], nums[left], nums[right]])
        #                 left += 1
        #                 right -= 1

        #                 # skip the duplicates
        #                 while left < right and nums[left] == nums[left - 1]:
        #                     left += 1

        #                 while left < right and nums[right] == nums[right + 1]:
        #                     right -= 1

        # return ans

        # using hashset
        n = len(nums)
        st = set()

        # checking all possible quadruplets:
        for i in range(n):
            for j in range(i+1, n):
                hashset = set()
                for k in range(j+1, n):
                    # taking bigger data type to avoid integer overflow:
                    sum_ = nums[i] + nums[j] + nums[k]
                    fourth = target - sum_
                    if fourth in hashset:
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        st.add(tuple(temp))
                    # put the kth element into the hashset:
                    hashset.add(nums[k])

        ans = [list(t) for t in st]
        return ans

                