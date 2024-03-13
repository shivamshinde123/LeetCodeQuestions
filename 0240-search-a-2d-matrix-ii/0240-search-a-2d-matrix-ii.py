class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        i, j = 0, len(matrix[0]) - 1
        
        
        while i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]):
            
            if matrix[i][j] == target:
                return True
            
            if matrix[i][j] < target:
                i += 1
            else:
                j -= 1
                
        return False
        
        
        
        
        
        