class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = list()
        is_numeric = lambda x: x.replace('.', '', 1).replace('-', '', 1).isdigit()
        for i in range(len(operations)):
            if is_numeric(operations[i]):
                scores.append(int(operations[i]))
            elif operations[i] == '+':
                scores.append(int(scores[-1]) + int(scores[-2]))
            elif operations[i] == 'D':
                scores.append(2*int(scores[-1]))
            else:
                scores.pop()
        return sum(scores)
                