class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        output = 0
        seen = []

        for _ in range(rows):
            temp = [False] * cols
            seen.append(temp)

        def bfs(r, c):

            seen[r][c] = True
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)] 
            queue = collections.deque()
            queue.append((r,c))

            while queue:
                row, col = queue.popleft()

                for dr, dc in dirs:
                    nr = row + dr
                    nc = col + dc
                    if (0 <= nr < rows and  0 <= nc < cols and 
                        not seen[nr][nc] and grid[nr][nc] == "1"
                        ):
                        seen[nr][nc] = True
                        queue.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not seen[r][c]:
                    output += 1
                    bfs(r, c)

        return output