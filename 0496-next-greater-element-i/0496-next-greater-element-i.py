class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        answer = list()
        for elem in nums1:
            ind_in_nums2 = nums2.index(elem)

            if ind_in_nums2 == len(nums2)-1:
                answer.append(-1)
                continue

            arr_after_elem_in_nums2 = nums2[ind_in_nums2+1:]
            if elem > max(arr_after_elem_in_nums2):
                answer.append(-1)
                continue

            for item in arr_after_elem_in_nums2:
                if item > elem:
                    answer.append(item)
                    break


        return answer
            