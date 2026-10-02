class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [ set() for i in range(9) ]
        cols = [ set() for i in range(9) ]
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                coord = (r // 3, c // 3)
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[coord]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[coord].add(board[r][c])
        
        return True