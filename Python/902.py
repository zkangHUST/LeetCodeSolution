class Solution:
    def atMostNGivenDigitSet(self, D, N):
        cnt = self.get(N)
        self.ans = self.count(cnt, D)
        # print(self.ans)
        target = list(str(N))
        self.dfs(D, target, 0)
        return self.ans      
    def get(self, N):
        cnt = 0
        while N:
            cnt += 1
            N = N // 10
        return cnt
    def count(self, N, D):
        i = 1
        ans = 0
        while i < N:
            ans += len(D) ** i
            i += 1
        return ans

    def dfs(self, D, target, cnt):
        if cnt == len(target):
            return 
        for val in D:
            if val < target[cnt]:
                self.ans += len(D) ** (len(target) - cnt - 1)
            elif val == target[cnt]:
                if cnt == len(target) - 1:
                    self.ans += 1
                self.dfs(D, target, cnt + 1)

D = ["5","6"]
N = 19
p = Solution()
ans = p.atMostNGivenDigitSet(D, N)
print(ans)
