class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        INF = 2147483647

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r,c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc

                if min(r,c) < 0 or r >= ROW or c >= COL or grid[r][c] != INF:
                    continue

                grid[r][c] = 1 + grid[row][col]
                q.append((r,c))
