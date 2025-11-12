class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        # Approach 1 - we can have maximum of 2 such elements
        # n = len(nums)
        # freq = dict()
        # result = list()

        # for i in range(n):
        #     if nums[i] not in freq:
        #         freq[nums[i]] = 1
            
        #     else: 
        #         freq[nums[i]] += 1


        # for item, value in freq.items():
        #     if len(result) == 2: # break the loop when the length of result is equal to 2
        #         break

        #     if value > n // 3:
        #         result.append(item)

        # return result
        
        # Approach 2 - simplified version of approach 1
        n = len(nums)
        min = n // 3
        freq = dict()
        result = list()

        for i in range(n):
            if len(result) == 2:
                break 

            if nums[i] not in freq:
                freq[nums[i]] = 1
            
            else: 
                freq[nums[i]] += 1

            if nums[i] not in result and freq[nums[i]] > min:
                result.append(nums[i])

        return result

        