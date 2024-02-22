class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        # Approach 1: checking all the possible patterns
#         winning_patterns = [[[0,0], [1,0], [2,0]], [[0,1], [1,1], [2,1]], [[0,2], [1,2], [2,2]], 
#                          [[0,0], [0,1], [0,2]], [[1,0], [1,1], [1,2]], [[2,0], [2,1], [2,2]],
#                          [[0,0], [1,1], [2,2]], [[0,2], [1,1], [2,0]]]
        
#         A_moves = list()
#         B_moves = list()
        
#         for i in range(len(moves)):
#             if i % 2 == 0:
#                 A_moves.append(moves[i])
#             else:
#                 B_moves.append(moves[i])
                
#         for pattern in winning_patterns:
#             if pattern[0] in A_moves and pattern[1] in A_moves and pattern[2] in A_moves:
#                 return 'A'
            
#             if pattern[0] in B_moves and pattern[1] in B_moves and pattern[2] in B_moves:
#                 return 'B'
            
#         if len(moves) == 9:
#             return 'Draw'
        
#         return 'Pending'
    
    
        # Approach 2
#         There are 8 ways to win for each player:

#         3 columns
#         3 rows
#         2 diagonals

#         Players make moves one by one so all even moves are for player A, odd for B.
#         Now we just need to track if we reach 3 in any line for any of the players.
#         One array keeps all ways to win for each player:

#         0,1,2 - for rows
#         3,4,5 - for cols
#         6 - for diagonal top left - bottom right (principal diagonal)
#         7 - for diagonal top right - bottom left (another diagonal)

        A = [0]*8
        B = [0]*8
        
        for i in range(len(moves)):
            move = moves[i]
            row, col = move[0], move[1]
            
            if i % 2 == 0:
                player = A
            else:
                player = B
                
            player[row] += 1
            player[col+3] += 1
            
            if row == col:
                player[6] += 1
                
            if row == 2 - col:
                player[7] += 1
                
            
        if 3 in A:
            return 'A'

        if 3 in B:
            return 'B'
        
        if len(moves) == 9:
            return 'Draw'
        
        return 'Pending'
            
            
        
        
        