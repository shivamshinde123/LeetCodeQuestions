class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        xor1 = 0
        xor2 = 0
        n = len(nums) 
        for i in range(n):
            xor1 = xor1 ^ nums[i] # xor of array elements
            xor2 = xor2 ^ i  # xor of number from 1 to n + 1

        xor2 = xor2 ^ n # xor of xor1 and xor2

        return xor1 ^ xor2

        

        