class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Handling duplicates across
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] in seen:
                    return False
                elif board[i][j] != '.':
                    seen.add(board[i][j])

        # Handling vertical duplicates
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen:
                    return False
                elif board[j][i] != '.':
                    seen.add(board[j][i])

        # Handling squares:
        for rmult in range(3):
            for cmult in range(3):
                seen = set()
                r = 3 * rmult
                c = 3 * cmult
                for i in range(r, r + 3):
        
                    for j in range(c, c + 3):
                        
                        if board[i][j] in seen:
                            return False
                        elif board[i][j] != '.':
                            seen.add(board[i][j])
        
        return True