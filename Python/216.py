class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        path = []
        self.get(n, 0, 0, k, 1, path)
        return self.ans
    def get(self, target, cur, cnt, k, begin, path):
        if cur > target or begin > 10:
            return 
        if cnt == k and target == cur:
            if path not in self.ans:
                self.ans.append(path)
            return 
        if cur + begin > target:
            return 
        for val in range(begin, 10):
            path.append(val)
            self.get(target, cur + val, cnt + 1, k, val + 1, path[:])
            path.pop()