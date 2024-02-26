class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        d = dict()
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        for i in range(1,27):
            d[i] = alpha[i-1]
            
        answer = list()
        
        while columnNumber != 0:
            rem = columnNumber % 26
            
            if rem == 0:
                answer.append('Z')
                columnNumber = columnNumber//26 - 1
            else:
                answer.append(d[rem])
                columnNumber //= 26
                
        return ''.join(answer)[::-1]
                
        
            