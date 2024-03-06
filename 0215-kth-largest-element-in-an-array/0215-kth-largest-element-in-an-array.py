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

        # Approach 3: Using quickselect algorithm  (GETTING TIME LIMIT EXCEEDED ERROR, COULDN'T FIGURE OUT WHY)
        # [arr[1]...arr[i]] -- Region 1 (less than or equal to pivot)
        # [arr[i+1]...arr[j-1]] -- Region 2 (greater than pivot)
        # [arr[j]...arr[n-1]] -- Unprocessed Region
        # arr[n] -- pivot
        
        # Initially, Region1 and Region2 are empty and Unprocessed Region == Whole array and
        # i = 0 and j = 1
        
        def Partition(arr, leftIndex, rightIndex, pivotIndex):
            pivot = nums[pivot_index]
            nums[pivot_index], nums[rightIndex] = nums[rightIndex], nums[pivot_index]
            stored_index = leftIndex
            for i in range(leftIndex, rightIndex): 
                if nums[i] < pivot:
                    nums[i], nums[stored_index] = nums[stored_index], nums[i]
                    stored_index += 1
            nums[rightIndex], nums[stored_index] = nums[stored_index], nums[rightIndex]
            return stored_index


        n = len(nums)
        
        if n < 2:
            return nums[0]
    
        leftIndex, rightIndex = 0, n - 1
        # kth largest == (n-k) smallest
        index = n - k # index of (n-k)th smallest element
    
        while True:
            pivot_index = random.randint(leftIndex, rightIndex)
            new_pivot_index = Partition(nums, leftIndex, rightIndex, pivot_index)
            if new_pivot_index == index:
                return nums[new_pivot_index]
            elif new_pivot_index > index:
                right = new_pivot_index - 1
            else:
                left = new_pivot_index + 1
        
        
        
