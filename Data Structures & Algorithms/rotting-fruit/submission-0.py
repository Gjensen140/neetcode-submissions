from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        output = 0
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c, m = queue.popleft()

            output = max(output, m)

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows) and (0 <= nc < cols):
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc, m + 1))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return output
