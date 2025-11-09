class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = list()
        neg = list()

        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        ans = list()
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])

        return ans