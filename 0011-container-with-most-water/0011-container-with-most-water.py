class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Approach 1: Time limit exceeded
        # max_volumn = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         volumn = (j-i) * min(height[j],height[i])
        #         if volumn > max_volumn:
        #             max_volumn = volumn

        # return max_volumn


        # Appraoch 2: two-pointer technique
        left = 0
        right = len(height) - 1
        max_vol = 0

        while left < right:
            current_vol = (right - left) * min(height[left], height[right])
            max_vol = max(max_vol, current_vol)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return max_vol
