class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        
        for instruction in instructions:
            if instruction == 'R':
                dx, dy = dy, -dx
            elif instruction == 'L':
                dx, dy = -dy, dx
            else:
                x, y = x + dx, y + dy
                
        return (x, y) == (0, 0) or (dx, dy) != (0,1)