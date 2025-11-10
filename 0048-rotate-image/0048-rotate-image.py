class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Brute force approach: 
        # - Create a new 2D array and then do the rest of the opeations
        
        # Optimal approach: first column of original array = reverse of transpose first row of rotated array

        # transpose an array
        m = len(matrix) # no. of rows

        for i in range(m):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse the rows
        for i in range(m):
            matrix[i].reverse()