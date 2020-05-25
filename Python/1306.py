class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        tmp = [start]
        visited = set()
        while True:
            new = []
            if not tmp:
                return False 
            for i in tmp:
                if arr[i] == 0:
                    return True
                visited.add(i)
                a = i + arr[i]
                b = i - arr[i] 
                if a >= 0 and a < len(arr) and a not in visited:
                    new.append(a)
                if b >= 0 and b < len(arr) and b not in visited:
                    new.append(b)
            tmp = new[:]