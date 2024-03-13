class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            
        def bsearch(arr, target):
            n = len(arr)
        
            left, right = 0, n - 1

            while left <= right:
                mid = (left + right) // 2
                mid_value = arr[mid]

                if mid_value == target:
                    return True

                if mid_value > target:
                    right = mid - 1

                if mid_value < target:
                    left = mid + 1

            return False
            
        for arr in matrix:
            if bsearch(arr, target):
                return True
        
        return False
        