class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        ## Approach 1
        # if len(arr) < 1:
        #     return arr

        # if len(arr) == 1:
        #     return [1]
        
        # arr1 = sorted(arr)
        # ranks = dict()
        # ranks[arr1[0]] = 1
        # for i in range(1, len(arr1)):
        #     prev_elem_rank = ranks[arr1[i-1]]
        #     if arr1[i] == arr1[i-1]:
        #         ranks[arr1[i]] = prev_elem_rank
        #     else:
        #         ranks[arr1[i]] = prev_elem_rank + 1

        # return [ranks[element] for element in arr]

        # Approach 2
        ranks = dict()
        sorted_arr = sorted(set(arr))

        for i in range(len(sorted_arr)):
            ranks[sorted_arr[i]] = i + 1

        return [ranks[elem] for elem in arr]

