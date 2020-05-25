# 超时
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.safe = set()
        self.notsafe = set()
        self.issafe = True
        for i in range(len(graph)):
            if i in self.safe:
                continue
            path = []
            self.dfs(graph, path, i)
            if not self.issafe:
                self.notsafe.add(i)
            else:
                for v in path:
                    self.safe.add(v)
            self.issafe = True
        # print(self.safe)
        return sorted(list(self.safe))
    def dfs(self, graph, path, i):
        if i in path:
            for v in path:
                self.notsafe.add(v)
            self.issafe = False
            return 
        path.append(i)
        if i in self.notsafe:
            for v in path:
                self.notsafe.add(v)
            self.issafe = False
        if i in self.safe:
            return
        for v in graph[i]:
            self.dfs(graph, path[:], v)
