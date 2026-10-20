from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = []
        count = 0

        for _ in range(rows):
            row = [False] * cols
            visited.append(row)

        # BFS:
        def bfs(r, c):

            queue = deque()
            queue.append((r, c))

            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            while queue:
                row, col = queue.popleft()

                for dr, dc in dirs:
                    nr = row + dr
                    nc = col + dc
                    if (0 <= nr < rows) and (0 <= nc < cols) and (grid[nr][nc] == '1' and not visited[nr][nc]):
                        
                        visited[nr][nc] = True
                        queue.append((nr, nc))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    visited[r][c] = True
                    bfs(r, c)
                    count += 1
        
        return count