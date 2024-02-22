class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        n = len(mat)
        required_sum = 0
        
        for i in range(n):
            required_sum += mat[i][i]
            required_sum += mat[i][n-1-i]
            
        return required_sum if n % 2 == 0 else required_sum - mat[n//2][n//2]