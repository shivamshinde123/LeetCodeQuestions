class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        # Approach 1: 
#         freq = dict()
        
#         for elem in nums:
#             freq[elem] = freq.get(elem, 0) + 1
            
#         degree = max(freq.values())

#         keys_of_degree = list()
#         for key, value in freq.items():
#             if value == degree:
#                 keys_of_degree.append(key)
                
#         def Dist(elem):
#             arr = list()
#             for i, num in enumerate(nums):
#                 if num == elem:
#                     arr.append(i)
                    
#             return arr[-1] - arr[0] + 1
        
#         shortestDistance = math.inf
#         for key in keys_of_degree:
#             shortestDistance = min(shortestDistance, Dist(key))
            
#         return shortestDistance


        # Approach 2    
        first_occurence_index = dict()
        freq = dict()
        result = 0
        degree = 0
        
        for i, num in enumerate(nums):
            first_occurence_index.setdefault(num, i)
            freq[num] = freq.get(num, 0) + 1
            
            if freq[num] > degree:
                degree = freq[num]
                result = i - first_occurence_index[num] + 1
            elif freq[num] == degree:
                result = min(result, i-first_occurence_index[num]+1)
            
        return result
    
        
            