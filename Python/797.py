class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.ans = []
        path = []
        self.dfs(path, graph, 0, len(graph) - 1)
        return self.ans
    
    def dfs(self, path, graph, node, target):
        path.append(node)
        if node == target:
            self.ans.append(path[:])
            return 
        for n in graph[node]:
            self.dfs(path[:], graph, n, target)