class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x, y = 0, 0
        for i in range(len(coordinates) - 1):
            if x == 0 and  y == 0:
                x, y = self.check(coordinates[i], coordinates[i + 1])
            else:
                x1, y1 = self.check(coordinates[i], coordinates[i + 1])
                if x1 * y != y1 * x:
                    return False
                x, y = x1, y1
        return True
    
    def check(self, p1, p2):
        return [p1[0] - p2[0], p1[1] - p2[1]]
    