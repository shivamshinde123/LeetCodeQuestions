class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # Approach 1
        # nums = list(map(lambda x: x**2, nums))
        # return sorted(nums)

        # Approach 2: two pointers
        l, r = 0, len(nums)-1
        answer = list()

        while l <= r:
            if abs(nums[r]) > abs(nums[l]):
                answer.append(nums[r]**2)
                r -= 1

            else:
                answer.append(nums[l]**2)
                l += 1
        
        return answer[::-1]
