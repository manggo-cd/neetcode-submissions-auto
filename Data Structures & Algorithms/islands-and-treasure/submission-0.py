class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        INF = 2147483647

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c))

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:

                row, col = r + dr, c + dc

                if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != INF:
                    continue

                grid[row][col] = grid[r][c] + 1
                q.append((row,col))