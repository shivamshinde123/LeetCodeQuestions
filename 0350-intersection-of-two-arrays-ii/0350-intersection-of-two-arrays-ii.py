class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Approach 1
        # answer = list()

        # for element in nums1:
        #     if element in nums2:
        #         answer.append(element)
        #         nums2.remove(element)
            
        # return answer

        # Approach 2: dictionary
        # freq = Counter(nums1)
        # answer = list()

        # for element in nums2:
        #     if (element in freq) and (freq[element] > 0):
        #         answer.append(element)
        #         freq[element] -= 1
        
        # return answer

        # Approach 3: using two pointer
        nums1.sort()
        nums2.sort()

        i, j = 0, 0
        answer = list()

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                answer.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return answer


