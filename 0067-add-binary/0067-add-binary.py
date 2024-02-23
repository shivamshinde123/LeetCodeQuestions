class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        answer = list()
        def DecimalToBinary(num):
            if num >= 1:
                DecimalToBinary(num // 2)
            answer.append(str(num % 2))
            
        def BinaryToDecimal(str_num):
            val = 0
            n = len(str_num)
            
            for i in range(n):
                if str_num[i] == '1':
                    val += 2 ** (n - 1 - i)
                    
            return val
        
        a = BinaryToDecimal(a)
        b = BinaryToDecimal(b)
        
        DecimalToBinary(a+b)
                
        
        print(answer)
        
        return str(int(''.join(answer)))
                