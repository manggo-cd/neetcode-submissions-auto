class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(i, opn, cls):
            if len(path) == 2*n:
                res.append("".join(path))
                return

            if opn < n:
                path.append("(")
                dfs(i, opn + 1, cls)
                path.pop()

            if cls < opn:
                path.append(")")
                dfs(i, opn, cls + 1)
                path.pop()
        
        dfs(0, 0, 0)
        return res



            