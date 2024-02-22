class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        n = len(mat)
        required_sum = 0
        
        for row in range(n):
            for col in range(n):
                if row == col or row == n - 1 - col:
                    required_sum += mat[row][col]
        
        return required_sum