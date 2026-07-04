class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set(),set(),set(),set(),set(),set(),set(),set(),set()]
        cols=[set(),set(),set(),set(),set(),set(),set(),set(),set()]
        cells=[set(),set(),set(),set(),set(),set(),set(),set(),set()]
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col]=='.':
                    continue
                if board[row][col] not in rows[row]:
                    rows[row].add(board[row][col])
                else: 
                    return False

                if board[row][col] not in cols[col]:
                    cols[col].add(board[row][col])
                else:
                    return False

                                # Check 3x3 box
                cell = (row // 3) * 3 + (col // 3)

                if board[row][col] in cells[cell]:
                    return False
                cells[cell].add(board[row][col])
        return True


