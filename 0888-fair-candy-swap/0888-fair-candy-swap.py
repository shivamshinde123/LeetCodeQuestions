class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:

        """
        k1 : alice gave to bob
        k2: bob gave to alice
        n1: total candy alice have
        n2: total candy bob have

        n1 + k2 - k1 = n2 + k1 - k2
        k1 = (k2 + (n1-n2)/2)
        """
        
        n1 = sum(aliceSizes)
        n2 = sum(bobSizes)
        n = (n1 - n2)/2

        for j in range(len(bobSizes)):
            if n + bobSizes[j] in aliceSizes:
                return [n + bobSizes[j], bobSizes[j]]