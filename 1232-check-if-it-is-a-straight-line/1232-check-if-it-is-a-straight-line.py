class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        n = len(coordinates)
        
        if n < 3:
            return True
        
        first = coordinates[0]
        last = coordinates[n-1]
        
        x1 = first[0]
        y1 = first[1]
        
        dx = last[0] - first[0]
        dy = last[1] - first[1]
        
        for coordinate in coordinates:
            
            x = coordinate[0]
            y = coordinate[1]
            
            ## VERY CLEVER SOLUTION: WE ARE USING MULTIPLICATION FORM OF EQUATION INSTEAD OF DIVISION FORM TO AVOID DIVISION BY ZERO ERROR
            if dx * (y - y1) != dy * (x - x1):
                return False
            
        return True
            
        
            
                
        
            