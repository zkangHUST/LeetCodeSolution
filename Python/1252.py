class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        a, b = set(), set()
        for idx in indices:
            if idx[0] not in a:
                a.add(idx[0])
            else:
                a.remove(idx[0])
            if idx[1] not in b:
                b.add(idx[1])
            else:
                b.remove(idx[1])
        
        return len(a) * m + len(b) * n - len(a) * len(b) * 2