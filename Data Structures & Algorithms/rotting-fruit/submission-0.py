class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0
        fresh = 0

        # want to find rotten fruit
        # from those sources, we want to keep traversing each level

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
                        continue

                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1

            time += 1

        return time if fresh == 0 else -1