class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def isPali(c):
            if c == c[::-1]:
                return True

        def dfs(i):
            if i == len(s):
                res.append(path.copy())
                return

            for j in range(i + 1, len(s) + 1):
                if isPali(s[i:j]):
                    path.append(s[i:j])
                    dfs(j)
                    path.pop()

        dfs(0)
        return res
