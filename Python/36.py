class Solution:
    def isValidSudoku(self, board):
        s = set()
        for i in range(len(board)):
            s.clear()
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
        for j in range(len(board[0])):
            s = set()
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                if not self.check(board, i, j):
                    return False
        return True


    def check(self, board, m, n):
        s = set()
        for i in range(m, m + 3):
            for j in range(n, n + 3):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
        return True


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

p = Solution()

ans = p.isValidSudoku(board)
print(ans)