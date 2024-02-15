class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Approach 1
        # answer = list()
        # s1 = set(nums1)
        # s2 = set(nums2)
        
        # for element in s1:
        #     if element in s2:
        #         answer.append(element)

        # return answer

        # Approach 2
        answer = list()
        s1 = list(set(nums1))
        s2 = list(set(nums2))

        s1.sort()
        s2.sort()

        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                answer.append(s1[i])
                i += 1
                j += 1
            elif s1[i] < s2[j]:
                i += 1
            else:
                j += 1

        return answer
