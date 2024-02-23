class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        # Approach 1
#         def get_number(string):
#             number = list()
#             for char in string:
#                 number.append(int(char))
            
#             number = sum([10**(len(number) - 1- i)*number[i] for i in range(len(number))])
#             return number
        
#         num1 = get_number(num1)
#         num2 = get_number(num2)
        
#         return str(num1*num2)


        # Approach 2
        """
        Lets's take an example of multiplication 
        
        23 * 45 = 5 * (10^0) * 3 * (10^0) + 5 * (10^0) * 2 * (10^1) + 4 * (10^1) * 3 * (10^0) + 4 * (10^1) * 2 * (10^1)
        
        we will use this logic to write the code
        """
        
        product = 0
        
        carry1 = 1
        
        for i in num1[::-1]:
            carry2 = 1
            
            for j in num2[::-1]:
                
                product += int(i) * carry1 * int(j) * carry2
                carry2 *= 10
            
            carry1 *= 10
            
        return str(product)
                
        