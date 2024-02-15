class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        c1 = dict()
        for elem in arr1:
            c1[elem] = c1.get(elem, 0) + 1

        answer = list()
        for elem in arr2:
            answer.extend([elem]*c1[elem])
            
        remaining = list()
        for elem in arr1:
            if elem not in arr2:
                remaining.append(elem)

        remaining.sort()

        return answer + remaining

