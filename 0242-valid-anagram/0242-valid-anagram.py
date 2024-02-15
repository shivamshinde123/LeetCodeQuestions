class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Approach 1: O(nlogn) time complexity due to mergesort
        # return self.merge_sort(s) == self.merge_sort(t)

        # Approach 2: O(n) time complexity
        if len(s) != len(t):
            return False

        s_dict = dict()
        t_dict = dict()

        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        return s_dict == t_dict

        

    def merge_two_sorted_arrays(self, a, b):
        sorted_array = list()
        len_a = len(a)
        len_b = len(b)
        i = j =0

        while (i < len_a and j < len_b):
            if ord(a[i]) <= ord(b[j]):
                sorted_array.append(a[i])
                i += 1
            else:
                sorted_array.append(b[j])
                j += 1

        while (i < len_a):
            sorted_array.append(a[i])
            i += 1

        while (j < len_b):
            sorted_array.append(b[j])
            j += 1

        return sorted_array

    def merge_sort(self, unsorted_str):
        unsorted_arr = list(unsorted_str)
        if len(unsorted_arr) <= 1:
            return unsorted_arr

        mid = len(unsorted_arr) // 2

        ## recursive step
        left = unsorted_arr[:mid]
        right = unsorted_arr[mid:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self.merge_two_sorted_arrays(left, right)
