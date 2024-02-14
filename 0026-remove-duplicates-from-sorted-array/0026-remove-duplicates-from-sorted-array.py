class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Appraoch 1- running time: 78ms
        expectedNums = list(set(nums))
        expectedNums = self.mergeSort(expectedNums)
        nums[0 : len(expectedNums) + 1] = expectedNums
        return len(expectedNums)

        # Approach 2 - running time: 79ms
        # j = 1
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i - 1]:
        #         nums[j] = nums[i]
        #         j += 1
        # return j

    def merge_two_arr(self, arr1, arr2):
        merged_arr = list()
        i, j = 0, 0
        l1, l2 = len(arr1), len(arr2)

        while (i < l1) and (j < l2):
            if arr1[i] <= arr2[j]:
                merged_arr.append(arr1[i])
                i += 1
            else:
                merged_arr.append(arr2[j])
                j += 1

        while i < l1:
            merged_arr.append(arr1[i])
            i += 1

        while j < l2:
            merged_arr.append(arr2[j])
            j += 1

        return merged_arr

    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr

        middle_index = len(arr) // 2
        left_arr = arr[:middle_index]
        right_arr = arr[middle_index:]

        left_arr = self.mergeSort(left_arr)
        right_arr = self.mergeSort(right_arr)

        sorted_arr = self.merge_two_arr(left_arr, right_arr)
        return sorted_arr
