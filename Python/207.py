# 找环
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        visited = [0] * numCourses
        for m, n in prerequisites:
            graph[n].append(m)
        for i in range(numCourses):
            if self.dfs(graph, i, visited):
                return False
        return True
    def dfs(self, graph, i, visited):
        if visited[i] == 1:
            return True
        if visited[i] == 2:
            return False
        visited[i] = 1
        for v in graph[i]:
            if self.dfs(graph, v, visited):
                return True
        visited[i] = 2
        return False