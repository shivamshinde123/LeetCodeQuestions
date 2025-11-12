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
        # n = len(nums)
        # min = n // 3
        # freq = dict()
        # result = list()

        # for i in range(n):
        #     if len(result) == 2:
        #         break 

        #     if nums[i] not in freq:
        #         freq[nums[i]] = 1
            
        #     else: 
        #         freq[nums[i]] += 1

        #     if nums[i] not in result and freq[nums[i]] > min:
        #         result.append(nums[i])

        # return result

        # Approach 2: Extended Moore's voting algorithm
        n = len(nums)
        cnt1, cnt2, ele1, ele2 = 0, 0, None, None

        for i in range(n):

            if cnt1 == 0 and nums[i] != ele2:
                cnt1 = 1
                ele1 = nums[i]

            elif cnt2 == 0 and nums[i] != ele1:
                cnt2 = 1
                ele2 = nums[i]

            elif ele1 == nums[i]:
                cnt1 += 1

            elif ele2 == nums[i]:
                cnt2 += 1

            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 = 0, 0

        for i in range(n):
            if nums[i] == ele1:
                cnt1 += 1
            
            if nums[i] == ele2:
                cnt2 += 1

        min = n // 3

        result = list()

        if cnt1 > min:
            result.append(ele1)

        if cnt2 > min: 
            result.append(ele2)

        return result

        