class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        pos = []
        for i in range(len(S)):
            if S[i] == C:
                pos.append(i)
        i, j = 0, 0
        res = []
        while i < len(S):
            if j == len(pos):
                res.append(i - pos[-1])
                i += 1
                continue
            if i <= pos[j]:
                if j == 0:
                    res.append(pos[j] - i)
                else:
                    tmp = min(pos[j] - i, i - pos[j - 1])
                    res.append(tmp)
                i += 1
            else:
                j += 1
        return res      