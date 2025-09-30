class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        temp = nums[-k:]
        for i in range(n-k-1, -1, -1):
            if n >= k:
                nums[i+k] = nums[i]
            else:
                nums[(i+k)%n] = nums[i]

        for i in range(k):
            nums[i] = temp[i]

