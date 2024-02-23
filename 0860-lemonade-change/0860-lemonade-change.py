class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        # Approach 1
#         change = dict()
        
#         for bill in bills:
#             change[bill] = change.get(bill, 0) + 1
            
#             if bill == 10:
#                 if change.get(5, 0) == 0:
#                     return False
#                 elif change.get(5, 0) > 0:
#                     change[5] -= 1
                    
#             elif bill == 20:
#                 if change.get(5, 0) >= 1 and change.get(10, 0) >= 1:
#                     change[5] -= 1
#                     change[10] -= 1
#                 elif change.get(5, 0) >= 3:
#                     change[5] -= 3
#                 else:
#                     return False
        
#         return True

        # Approach 2
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True