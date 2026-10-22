# Intuition: BFS outward from a treasure chest

from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        rows = len(grid)
        cols = len(grid[0])


        queue = deque()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                # Found a treasure chest
                if grid[r][c] == 0: 
                    queue.append((r, c))

        
        while queue:
            row, col = queue.popleft()

            for dr, dc in dirs:
                nr = dr + row
                nc = dc + col

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == inf
                    ):
                    grid[nr][nc] = (grid[row][col] + 1)
                    queue.append((nr, nc))