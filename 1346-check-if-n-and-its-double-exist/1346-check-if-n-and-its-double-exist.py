class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        arr = list(map(float, arr))

        for i in range(len(arr)):
            elem = arr[i]
            condition = (elem / 2 in arr[:i]) or (elem / 2 in arr[i+1:])

            if condition:
                return condition
