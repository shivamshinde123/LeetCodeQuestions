class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        winning_patterns = [[[0,0], [1,0], [2,0]], [[0,1], [1,1], [2,1]], [[0,2], [1,2], [2,2]], 
                         [[0,0], [0,1], [0,2]], [[1,0], [1,1], [1,2]], [[2,0], [2,1], [2,2]],
                         [[0,0], [1,1], [2,2]], [[0,2], [1,1], [2,0]]]
        
        A_moves = list()
        B_moves = list()
        
        for i in range(len(moves)):
            if i % 2 == 0:
                A_moves.append(moves[i])
            else:
                B_moves.append(moves[i])
                
        for pattern in winning_patterns:
            if pattern[0] in A_moves and pattern[1] in A_moves and pattern[2] in A_moves:
                return 'A'
            
            if pattern[0] in B_moves and pattern[1] in B_moves and pattern[2] in B_moves:
                return 'B'
            
        if len(moves) == 9:
            return 'Draw'
        
        return 'Pending'
        
        
        
        