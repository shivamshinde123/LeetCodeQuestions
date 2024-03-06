class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Approach 1
        # nums.sort(reverse=True)
        # return nums[k-1]
        
        # Approach 2: using heap
#         n = len(nums)
#         heapq.heapify(nums)
        
#         for i in range(n-k):
#             heapq.heappop(nums)
        
#         kth_largest = heapq.heappop(nums)
#         return kth_largest

        # Using quickselect algorithm
        def partition(nums, low, high):
            pivot = nums[low]
            i, j = low + 1, high
            
            while i <= j:
                if nums[i] < pivot and pivot < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
                if nums[i] >= pivot:
                    i += 1
                if pivot >= nums[j]:
                    j -= 1
            
            nums[low], nums[j] = nums[j], nums[low]
            return j
        
        low, high = 0, len(nums) - 1
        pivotIndex = len(nums)
        
        while pivotIndex != k - 1:
            pivotIndex = partition(nums, low, high)
            if pivotIndex < k - 1:
                low = pivotIndex + 1
            else:
                high = pivotIndex - 1
        
        return nums[k - 1]
        
        
        