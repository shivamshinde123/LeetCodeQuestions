class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        num_freq = {i:0 for i in range(1,len(nums)+1)}
        for num in nums:
            num_freq[num] += 1

        answer = [0]*2
        for num in num_freq:
            if num_freq[num] == 0:
                answer[1] = num
            elif num_freq[num] == 2:
                answer[0] = num
     
        return answer