class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dis = [float("inf") for i in range(N)]
        dis[K - 1] = 0
        for i in range(N):
            for t in times:
                u, v, w = t[0], t[1], t[2]
                dis[v - 1] = min(dis[v - 1], dis[u - 1] + w)
        m = max(dis)
        if m == float("inf"):
            return -1
        return m