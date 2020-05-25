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
        visited = set()
        return self.dfs(g, visited, start, target)
    def dfs(self, g, visited, start, target):
        if start == target:
            return True
        if start in visited:
            return False
        if start not in g:
            return False
        for v in g[start]:
            if v not in visited and self.dfs(g, visited, v, target):
                return True
        return False
