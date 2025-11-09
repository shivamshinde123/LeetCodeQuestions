class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        # Brute force approach
        # pos = list()
        # neg = list()

        # for num in nums:
        #     if num > 0:
        #         pos.append(num)
        #     else:
        #         neg.append(num)

        # ans = list()
        # for i in range(len(pos)):
        #     ans.append(pos[i])
        #     ans.append(neg[i])

        # return ans

        # Better appraoch
        n = len(nums)
        ans = [0] * n
        pos_index = 0
        neg_index = 1

        for i in range(n):
            if nums[i] > 0:
                ans[pos_index] = nums[i]
                pos_index += 2
            else:
                ans[neg_index] = nums[i]
                neg_index += 2

        return ans