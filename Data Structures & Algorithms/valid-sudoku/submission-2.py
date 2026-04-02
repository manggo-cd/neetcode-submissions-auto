class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # specify region
        # always a 9x9 board

        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in sqrs[(r//3, c//3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                sqrs[(r//3, c//3)].add(board[r][c])

        return True
