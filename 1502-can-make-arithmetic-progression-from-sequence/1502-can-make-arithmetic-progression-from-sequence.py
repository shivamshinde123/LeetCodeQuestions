class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        if len(arr) <= 1:
            return False
        
        arr.sort()
        
        diff = arr[1] - arr[0]
        start = arr[0]
        
        for i in range(len(arr)):
            if arr[i] != start + i*diff:
                return False
            
        return True