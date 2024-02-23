class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def get_number(string):
            number = list()
            for char in string:
                number.append(int(char))
            
            number = sum([10**(len(number) - 1- i)*number[i] for i in range(len(number))])
            return number
        
        num1 = get_number(num1)
        num2 = get_number(num2)
        
        return str(num1*num2)