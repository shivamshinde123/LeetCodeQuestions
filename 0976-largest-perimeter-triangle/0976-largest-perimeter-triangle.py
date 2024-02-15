class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        def is_triangle(a,b,c):
            return (a+b>c) and (b+c>a) and (c+a>b)

        nums.sort(reverse=True)

        for i in range(len(nums)-2):
            if is_triangle(nums[i], nums[i+1], nums[i+2]):
                return nums[i] + nums[i+1] + nums[i+2]

        return 0

        