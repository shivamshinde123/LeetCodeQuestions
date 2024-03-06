class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Approach 1
        # nums.sort(reverse=True)
        # return nums[k-1]
        
        # Approach 2: using heap
        n = len(nums)
        heapq.heapify(nums)
        
        for i in range(n-k):
            heapq.heappop(nums)
        
        kth_largest = heapq.heappop(nums)
        return kth_largest
        
        
        