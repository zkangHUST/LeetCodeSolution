class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        return self.dfs(rooms)
    def dfs(self, rooms):
        self.visited = [0] * len(rooms)
        self.visit(0, rooms)
        for v in self.visited:
            if v != 1:
                return False
        return True
    def visit(self, i, rooms):
        self.visited[i] = 1
        for v in rooms[i]:
            if self.visited[v] == 0:
                self.visit(v, rooms)
        
        


