class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix:
            return []
        
        
        answer = list()
        rows, cols = len(matrix), len(matrix[0])
        top, right, bottom, left = 0, cols - 1, rows - 1, 0
        step = 0
        
        while left <= right and top <= bottom:
            
            match (step % 4):
                
                case 0:
                    for i in range(left, right+1):
                        answer.append(matrix[top][i])
            
                    top += 1
                
                case 1:
                    for i in range(top, bottom+1):
                        answer.append(matrix[i][right])

                    right -= 1
                    
                case 2:
                    for i in range(right, left-1, -1):
                        answer.append(matrix[bottom][i])

                    bottom -= 1
                    
                case 3:
                    for i in range(bottom, top-1, -1):
                        answer.append(matrix[i][left])

                    left += 1
                    
            step += 1
            

        return answer
        
        