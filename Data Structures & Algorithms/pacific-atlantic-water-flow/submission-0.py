class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        res = []

        def dfs(row, col, path, prev):
            if (row, col) in path or row < 0 or col < 0 or row >= len(heights) or col >= len(heights[0]) or heights[row][col] < prev:
                return

            path.add((row, col))
            dfs(row + 1, col, path, heights[row][col])
            dfs(row, col + 1, path, heights[row][col])
            dfs(row - 1, col, path, heights[row][col])
            dfs(row, col - 1, path, heights[row][col])

        for r in range(len(heights)):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, len(heights[0]) - 1, atl, heights[r][len(heights[0]) - 1])

        for c in range(len(heights[0])):
            dfs(0, c, pac, heights[0][c])
            dfs(len(heights) - 1, c, atl, heights[len(heights) - 1][c])

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res

        
