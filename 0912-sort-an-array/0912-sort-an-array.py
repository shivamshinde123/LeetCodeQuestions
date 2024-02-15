class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ## Merge sort
        n = len(nums)

        if n <= 1:
            return nums

        mid = n//2
        left = nums[:mid]
        right = nums[mid:]

        left = self.sortArray(left)
        right = self.sortArray(right)

        return self.mergeTwoArray(left, right)

    def mergeTwoArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        lst = list()
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                lst.append(arr1[i])
                i += 1
            else:
                lst.append(arr2[j])
                j += 1
        
        while i < len(arr1):
            lst.append(arr1[i])
            i += 1

        while j < len(arr2):
            lst.append(arr2[j])
            j += 1

        return lst
