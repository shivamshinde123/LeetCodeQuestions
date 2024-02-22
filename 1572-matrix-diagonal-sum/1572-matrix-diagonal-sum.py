class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        # Approach 1
#         n = len(mat)
#         required_sum = 0
#         for i in range(n):
#             for j in range(n):
#                 if i == j or i == n - 1- j:
#                     required_sum += mat[i][j]
                    
#         return required_sum
        
        # Approach 2
        n = len(mat)
        required_sum = 0
        
        for i in range(n):
            required_sum += mat[i][i]
            required_sum += mat[i][n-1-i]
            
        # removing the value that is added twice which is present only when mat have odd number of rows
        return required_sum if n % 2 == 0 else required_sum - mat[n//2][n//2]