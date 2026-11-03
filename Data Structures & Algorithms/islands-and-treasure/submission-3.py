from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        
        # Used for checking
        inf = 2147483647

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            row, col = queue.popleft()

            for dr, dc in neighbors:
                nr = row + dr
                nc = col + dc

                if (0 <= nr < rows and 0 <= nc < cols and
                grid[nr][nc] == inf
                ):
                    grid[nr][nc] = 1 + grid[row][col]
                    queue.append((nr,nc))
