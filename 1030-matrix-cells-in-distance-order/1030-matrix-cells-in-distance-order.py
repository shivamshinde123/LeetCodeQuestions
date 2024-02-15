class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        
        answer = dict()
        for i in range(rows):
            for j in range(cols):
                answer[(i,j)] = abs(i-rCenter) + abs(j-cCenter)
        
        answer = sorted(answer.items(), key=lambda x: x[1])

        return dict(answer).keys()

        answer.sort()