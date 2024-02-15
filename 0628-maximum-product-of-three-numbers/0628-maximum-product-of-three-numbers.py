class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Approrach 1: using mergesort
        # nums = self.mergesort(nums)

        # Approach 2: using python's inbuilt sort function: faster
        nums.sort()
        n = len(nums)

        return max(nums[n-1]*nums[n-2]*nums[n-3], nums[0]*nums[1]*nums[n-1])

    def merge_two_array(self, arr1, arr2):

        i, j = 0, 0
        n1 = len(arr1)
        n2 = len(arr2)
        sorted_arr = list()
        while (i < n1) and (j < n2):
            if arr1[i] < arr2[j]:
                sorted_arr.append(arr1[i])
                i += 1
            else:
                sorted_arr.append(arr2[j])
                j += 1

        while (i < n1):
            sorted_arr.append(arr1[i])
            i += 1

        while (j < n2):
            sorted_arr.append(arr2[j])
            j += 1

        return sorted_arr

    def mergesort(self, arr):

        if len(arr) <= 1:
            return arr

        middle_index = len(arr) // 2

        left_arr = arr[:middle_index]
        right_arr = arr[middle_index:]

        left_arr = self.mergesort(left_arr)
        right_arr = self.mergesort(right_arr)

        return self.merge_two_array(left_arr, right_arr)
        
        
