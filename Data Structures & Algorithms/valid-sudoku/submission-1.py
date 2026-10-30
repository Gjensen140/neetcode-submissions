class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Checking horizontal correctness
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] in seen:
                    return False
                if board[i][j] != ".":
                    seen.add(board[i][j])
        
        # Checking vertical correctness
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen:
                    return False
                if board[j][i] != ".":
                    seen.add(board[j][i])


        sections = [[0,1,2], [3,4,5], [6,7,8]]

        for s1 in sections:
            for s2 in sections:
                seen = set()
                for i in s1:
                    for j in s2:
                        if board[i][j] in seen:
                            return False
                        if board[i][j] != ".":
                            seen.add(board[i][j])
                            
        return True