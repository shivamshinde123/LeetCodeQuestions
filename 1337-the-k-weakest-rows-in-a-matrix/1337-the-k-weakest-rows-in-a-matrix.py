class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        soldier_count = dict()

        for i in range(len(mat)):
            soldier_count[i] = sum(mat[i])

        soldier_count = dict(sorted(soldier_count.items(), key=lambda x:x[1]))
        return list(soldier_count.keys())[:k]