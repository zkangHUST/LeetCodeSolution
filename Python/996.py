class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        self.ans = []
        path = []
        visited = [0 for i in range(len(A))]
        self.dfs(A, 1, path, visited)
        return len(self.ans)
    def dfs(self, A, cnt, path, visited):
        if cnt > len(A):
            if path not in self.ans:
                self.ans.append(path)
            return
        tmp = set()
        for i in range(len(A)):
            if visited[i]  == 1:
                continue
            if A[i] in tmp:
                continue
            if path and not self.check(path[-1] + A[i]):
                continue
            tmp.add(A[i])
            visited[i] = 1
            path.append(A[i])
            self.dfs(A, cnt + 1, path[:], visited)
            path.pop()
            visited[i] = 0           
    def check(self, num):
        if num == 1 or num == 0:
            return True
        l, r = 1, num // 2
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == num:
                return True
            if mid * mid < num:
                l = mid + 1
            else:
                r = mid - 1
        return False