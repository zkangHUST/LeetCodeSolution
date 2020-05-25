class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        g = {}
        for v in graph:
            if v[0] == v[1]:
                continue
            if v[0] not in g:
                g[v[0]] = {v[1]}
            else:
                g[v[0]].add(v[1])
            # //visited = set()
        # print(g)
        path = []
        return self.dfs(g, path, start,target)
    def dfs(self, g, path, start, end):
        if start == end:
            return True
        if start in path:
            return False
        # visited.add(start)

        if start not in g:
            return False
        path.append(start)
        for v in g[start]:
            # print(path)
            ans = self.dfs(g, path[:], v, end)
            if ans:
                return True
        return False