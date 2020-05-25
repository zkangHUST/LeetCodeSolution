class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        m = {}
        visited = {src}
        for val in flights:
            s, e, c = val[0], val[1], val[2]
            if s not in m:
                m[s] = [[e, c]]
            else:
                m[s].append([e, c])
        ans = [float("inf")]
        self.dfs(m, src, dst, 0, K + 1, 0, visited, ans)
        if ans[0] != float("inf"):
            return ans[0]
        return -1

    def dfs(self, m, cur, dst, cnt, k, curcost, visited, ans):
        if cnt > k or (cnt == k and cur != dst):
            return
        if cur == dst:
            ans[0] = curcost
            return
        if cur not in m:
            return
        for v in m[cur]:
            end, cost = v[0], v[1]
            if end in visited:
                continue
            if curcost + cost >= ans[0]:
                continue
            visited.add(v[0])
            r = self.dfs(m, end, dst, cnt + 1, k, curcost + cost, visited, ans)
            visited.remove(v[0])