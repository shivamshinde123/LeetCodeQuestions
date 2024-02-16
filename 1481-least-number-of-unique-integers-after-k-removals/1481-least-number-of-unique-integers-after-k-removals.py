class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        arr_elem_freq = dict()
        
        for elem in arr:
            arr_elem_freq[elem] = arr_elem_freq.get(elem,0) + 1
            
        # sorting the arr_elem_freq using the values
        arr_elem_freq = dict(sorted(arr_elem_freq.items(), key=lambda x: x[1]))
        
        # now will remove the first k keys from the sorted arr_elem_freq
        for key in arr_elem_freq:
            if k > 0:
                val = arr_elem_freq[key]
                if val <= k:
                    k = k - val
                    arr_elem_freq[key] = 0
                else:
                    arr_elem_freq[key] = arr_elem_freq[key] - k
                    k = 0
                    
        return len(set([key for key, val in arr_elem_freq.items() if val != 0]))