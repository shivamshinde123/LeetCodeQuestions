class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        ## Approach 1: using inbuilt functions
        # n = len(nums)
        # return list(set(list(range(n,0,-1))).difference(nums))
        
        freq = {i:0 for i in range(1,len(nums)+1)}
        
        for elem in nums:
            freq[elem] += 1
            
        answer = list()
        for key in freq.keys():
            if freq[key] == 0:
                answer.append(key)
                
        return answer
            
        