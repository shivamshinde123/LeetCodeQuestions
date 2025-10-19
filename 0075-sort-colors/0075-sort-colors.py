class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # BUBBLE SORT - O(N^2)
        # n = len(nums)
        # k = n - 1
        # while k >= 0:
        #     for i in range(k):
        #         if nums[i] > nums[i+1]:
        #             nums[i], nums[i+1] = nums[i+1], nums[i]
        #     k -= 1
        
        # return nums

        # QUICK SORT - O(NLogN)
        # def partition(arr, low, high):
        #     pivot = arr[low]
        #     i = low
        #     j = high

        #     while (i < j):
        #         while (arr[i] <= pivot and i <= high-1):
        #             i +=1
        #         while (arr[j] > pivot and j >= low):
        #             j -= 1

        #         if (i < j):
        #             arr[i], arr[j] = arr[j], arr[i]
            
        #     arr[low], arr[j] = arr[j], arr[low]

        #     return j

        # def quicksort(arr, low, high):
        #     if (low < high):
        #         pIndex = partition(arr, low, high)
        #         quicksort(arr, low, pIndex-1)
        #         quicksort(arr, pIndex+1, high)

        # n = len(nums)
        # quicksort(nums, 0, n-1)

        # Approach 3
        # a = nums.count(0)
        # b = nums.count(1)
        # c = nums.count(2)

        # nums[:] =[0]*a + [1]*b + [2]*c

        # Approach 4
        n = len(nums)
        low, mid = 0, 0
        high = n - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


    
                

    