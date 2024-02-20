class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = list()
        
        for i in range(len(operations)):
            if operations[i].lstrip('-').isdigit():
                scores.append(int(operations[i]))
            elif operations[i] == '+':
                scores.append(int(scores[-1]) + int(scores[-2]))
            elif operations[i] == 'D':
                scores.append(2*int(scores[-1]))
            else:
                scores.pop()
            print(scores)
        return sum(scores)
                