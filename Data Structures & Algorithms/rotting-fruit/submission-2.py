class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        time = 0
        fresh = 0
        q = deque()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        directions = [[1,0], [-1,0], [0,-1], [0,1]]

        while fresh > 0 and q:
            for i in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = dr + row, dc + col

                    if min(r,c) < 0 or r >= ROW or c >= COL or grid[r][c] != 1:
                        continue

                    grid[r][c] = 2
                    fresh -= 1
                    q.append((r,c))
            
            time += 1
        
        return time if fresh == 0 else -1
        