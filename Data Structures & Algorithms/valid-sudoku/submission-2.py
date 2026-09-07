class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        for row in range(len(board)):
            for c in range(len(board[row])):
                if board[row][c] != '.':
                    if board[row][c] not in rows[row]:
                        rows[row].add(board[row][c])
                    else:
                        return False
                    if board[row][c] not in cols[c]:
                        cols[c].add(board[row][c])
                    else:
                        return False 
                    box=(row//3)*3+c//3
                    if board[row][c] not in boxes[box]:
                        boxes[box].add(board[row][c])
                    else: return False
        return True
