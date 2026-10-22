from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        output = 0


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            row, col, t = queue.popleft()

            for dr, dc in dirs:
                nr = dr + row
                nc = dc + col

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    output = max(t+1, output)
                    queue.append((nr, nc, t+1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return output
