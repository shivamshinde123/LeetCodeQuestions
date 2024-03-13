class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        search_lst = list()
        
        for lst in matrix:
            search_lst.extend(lst)
            
        n = len(search_lst)
        
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_value = search_lst[mid]
            
            if mid_value == target:
                return True
            
            if mid_value > target:
                right = mid - 1
                
            if mid_value < target:
                left = mid + 1
                
        return False
            