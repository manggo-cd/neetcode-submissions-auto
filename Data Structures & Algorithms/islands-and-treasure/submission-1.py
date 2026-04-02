class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        INF = 2147483647

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if min(nr, nc) < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] != INF:
                    continue
                grid[nr][nc] = 1 + grid[row][col]
                q.append((nr, nc))
