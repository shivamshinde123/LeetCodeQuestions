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
                
        # THIS PART IS KINDA CONFUSING
        return left + k
    
    
    
        