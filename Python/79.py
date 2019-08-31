class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        path = ""
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != word[0]:
                    continue
                if self.dfs(board, i, j, 0, word, visited[:], ""):
                    return True
        return False
    def dfs(self, board, i , j, cnt, word, visited, path):
        if cnt == len(word):
            if path == word:
                return True
            else:
                return False
        if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0:
            return False
        if visited[i][j] == 1:
            return False
        if board[i][j] != word[cnt]:
            return False
        visited[i][j] = 1
        if self.dfs(board, i - 1, j, cnt + 1, word, visited, path + board[i][j]):
            return True
        if self.dfs(board, i + 1, j, cnt + 1, word, visited, path + board[i][j]):
            return True
        if self.dfs(board, i, j - 1, cnt + 1, word, visited, path + board[i][j]):
            return True
        if self.dfs(board, i, j + 1, cnt + 1, word, visited, path + board[i][j]):
            return True
        visited[i][j] = 0
        return False