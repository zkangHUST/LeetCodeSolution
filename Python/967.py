class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        self.ans = []
        path = []
        self.get(0, N, K , path)
        print(self.ans)
        return self.ans
    def get(self, cnt, n, k, path):
        if cnt == n:
            s = 0
            for val in path:
                s = s * 10 + val
            if s not in self.ans:
                self.ans.append(s)
            return
        nums = [] 
        if cnt == 0:
            nums = [i for i in range(1, 10)]
        else:
            if 0 <= path[-1] + k <= 9:
                nums.append(path[-1] + k)
            if 0 <= path[-1] - k <= 9:
                nums.append(path[-1] - k)
        for val in nums:
            path.append(val)
            self.get(cnt + 1, n, k, path[:])
            path.pop()
p = Solution()
p.numsSameConsecDiff(3, 7)