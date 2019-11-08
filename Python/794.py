class Solution:
    def validTicTacToe(self, board):
        cnt1 = []
        cnt2 = []
        for s in board:
            cnt1.append(s.count('X'))
            cnt2.append(s.count('O'))
        if cnt1.count(3) or cnt2.count(3):
            return False
        if sum(cnt1) < sum(cnt2)  or sum(cnt1) - sum(cnt2) >= 2:
            return False
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i]:
                if board[0][i] == 'X':
                    if sum(cnt1) != sum(cnt2) + 1:
                        return False
                elif board[0][i] == 'O':
                    if (sum(cnt1) != sum(cnt2)):
                        return False
        if board[0][0] == board[1][1] == board[2][2]:
            return False
        if board[0][2] == board[1][1] == board[2][0]:
            return False
        return True

res = ["XXX","OOX","OOX"]
p = Solution()
print(p.validTicTacToe(res))

        