class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        change = dict()
        
        for bill in bills:
            change[bill] = change.get(bill, 0) + 1
            
            print(f"at start: {change}")
            
            if bill == 10:
                if change.get(5, 0) == 0:
                    return False
                elif change.get(5, 0) > 0:
                    change[5] -= 1
                    
            elif bill == 20:
                if change.get(5, 0) >= 1 and change.get(10, 0) >= 1:
                    change[5] -= 1
                    change[10] -= 1
                elif change.get(5, 0) >= 3:
                    change[5] -= 3
                else:
                    return False
                
            print(f"at end: {change}")
        
        return True