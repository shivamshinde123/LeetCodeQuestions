class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        left, right = 0, n - 1
        
        while left <= right:
            
            mid = (left + right) // 2
            missing_num_less_than_mid_value = arr[mid] - mid - 1
            
            if  missing_num_less_than_mid_value >= k:
                right = mid - 1
                
            if missing_num_less_than_mid_value < k:
                left = mid + 1
                
        return left + k
    
    
        # low = 0
        # high = len(arr) - 1
        # while low <= high:
        #     mid = (low + high) // 2
        #     missing = arr[mid] - (mid + 1)
        #     if missing < k:
        #         low = mid + 1
        #     else:
        #         high = mid - 1
        # return high + 1 + k
    
    
        