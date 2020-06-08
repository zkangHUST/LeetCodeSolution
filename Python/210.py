# 拓扑排序,找环
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        for m, n in prerequisites:
            graph[n].append(m)
        ans = []
        visited = [0 for i in range(numCourses)]
        for i in range(numCourses):
            if self.dfs(graph, i, visited, ans) :
                return []
        return ans
    def dfs(self, graph, i, visited, ans):
        if visited[i] == 1:
            return True
        if visited[i] == 2:
            return False
        visited[i] = 1
        for v in graph[i]:
            if self.dfs(graph, v, visited, ans):
                return True
        ans.insert(0, i)
        visited[i] = 2
        return False