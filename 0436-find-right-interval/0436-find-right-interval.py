class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        n = len(intervals)
        
        for i in range(n):
            intervals[i].append(i)
            
        
        def bsearch(target):
            
            left, right = 0, n - 1
            answer = float('inf')
            
            while left <= right:
                
                mid = (left + right) // 2
                mid_interval = intervals[mid]
                
                if mid_interval[0] >= target:
                    answer = min(mid, answer)
                    right = mid - 1
                    
                else:
                    left = mid + 1
                    
            return answer
        
        intervals.sort()
        result = [-1]*n
        for interval in intervals:
            end = interval[1]
            req_start_interval_index = bsearch(end)
            
            if req_start_interval_index != float('inf'):
                result[interval[2]] = intervals[req_start_interval_index][2]
        
        return result
        
                
         
                
            
            
        
            
            
        
            
        