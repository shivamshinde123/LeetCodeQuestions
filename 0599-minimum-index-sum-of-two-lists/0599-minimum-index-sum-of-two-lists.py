class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        # Approach 1
#         common_strings = dict()
        
#         for i in range(len(list1)):
#             if list1[i] in list2:
#                 j = list2.index(list1[i])
#                 common_strings[list1[i]] = i + j
                
#         min_index_sum = min(common_strings.values())
        
        
#         answer = list()
#         for string in common_strings:
#             if common_strings[string] == min_index_sum:
#                 answer.append(string)
                
#         return answer

        # Appraoch 2
        index_sum = math.inf
        common_strings = list()
        
        
        for i in range(len(list1)):
            if list1[i] in list2:
                j = list2.index(list1[i])
                if i + j < index_sum:
                    index_sum = i + j
                    common_strings.clear()
                    common_strings.append(list1[i])
                elif i + j == index_sum:
                    common_strings.append(list1[i])
                    
        return common_strings
                
        
                    
        