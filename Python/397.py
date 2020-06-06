class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.bfs(n)

    def bfs(self, n):
        if n == 1:
            return 0
        s = [n]
        cnt, ans, nextcnt = 1, 0, 0
        while len(s) > 0:
            top = s[0]
            s.pop(0)
            cnt -= 1
            if top == 1:
                return ans
            if top % 2 == 0:
                s.append(top / 2)
                nextcnt += 1
            else:
                s.append(top + 1)
                s.append(top -1)
                nextcnt += 2
            if cnt == 0:
                ans += 1
                cnt = nextcnt
                nextcnt = 0
        return ans