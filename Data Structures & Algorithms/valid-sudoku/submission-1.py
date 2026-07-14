class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set(),set(),set(),set(),set(),set(),set(),set(),set()]
        cols=[set(),set(),set(),set(),set(),set(),set(),set(),set()]
        boxes=[set(),set(),set(),set(),set(),set(),set(),set(),set()]
        for row in range (len(board)):
            for col in range (len(board)):
                if board[row][col] =='.':
                    pass
                else:
                    if board[row][col] in rows[row]:
                        return False
                    else:
                        rows[row].add(board[row][col])
                    if board[row][col] in cols[col]:
                        return False
                    else:
                        cols[col].add(board[row][col])
                    box=(row//3)*3+col//3
                    if board[row][col] in boxes[box]:
                        return False
                    else:
                        boxes[box].add(board[row][col])
        return True


