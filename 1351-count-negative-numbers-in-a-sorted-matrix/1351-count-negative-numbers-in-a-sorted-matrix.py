class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        def countNeg(arr):
            
            """
            This function will find the index of first negative number in an array and using it will find the count of total
            negative numbers in the same array. Note that at the end of while loop, left_index position will be the index of first
            negative number in an array.
            """
            
            n = len(arr)
            left_index, right_index = 0, n - 1
            
            total_negative = 0
            
            while left_index <= right_index:
                
                mid_index = left_index + (right_index - left_index) // 2
                mid_value = arr[mid_index]
                
                if mid_value >= 0:
                    left_index = mid_index + 1
                
                if mid_value < 0:
                    right_index = mid_index - 1
                    
            if left_index <= n - 1:
                return len(arr) - left_index
            else:
                return 0
        
        answer = 0
        for arr in grid:
            answer += countNeg(arr)
            
        return answer