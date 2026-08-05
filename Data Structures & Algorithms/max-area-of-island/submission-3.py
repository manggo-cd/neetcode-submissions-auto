class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    self.size = 0
                    self.dfs(grid, r, c)
                    maxArea = max(maxArea, self.size)

        return maxArea
        
    def dfs(self, grid, r, c):
        if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or grid[r][c] != 1:
            return
        self.size += 1
        grid[r][c] = 0
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r, c - 1)