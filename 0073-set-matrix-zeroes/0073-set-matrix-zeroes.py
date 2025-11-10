class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Approach1: O(m x n) and O(m + n)
        m = len(matrix) # no. of rows
        n = len(matrix[0]) # no. of columns

        rows = set()
        cols = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0

        # Approach 2: O(m x n) and O(1)
        # In this approach, instead of using O(mxn) space complexity, there is another solution, where we can use
        # first row and first colunn of an array as storage. 
        

                

        

        
        