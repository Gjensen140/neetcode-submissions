from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        output = 0

        rows = len(grid)
        cols = len(grid[0])

        seen = []


        for _ in range(rows):
            row = [False] * cols
            seen.append(row)
        
        def bfs(r, c):

            queue = deque()
            queue.append((r, c))
            
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            area = 1

            while queue:
                row, col = queue.popleft()

                for dr, dc in dirs:
                    nr = row + dr
                    nc = col + dc

                    if (0 <= nr < rows and 0 <= nc < cols) and (grid[nr][nc] == 1 and not seen[nr][nc]):
                        seen[nr][nc] = True
                        area += 1
                        queue.append((nr, nc))

            print(area)
            return area
                        


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not seen[r][c]:
                    seen[r][c] = True
                    area = bfs(r,c)
                    output = max(area, output)

        return output