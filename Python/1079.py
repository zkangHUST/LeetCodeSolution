# DFS
class Solution:
    def numTilePossibilities(self, tiles):
        cnt = {}
        for c in tiles:
            if c not in cnt:
                cnt[c] = 1
            else:
                cnt[c] += 1
        ret = self.dfs(cnt)
        return ret
    
    def dfs(self, cnt):
        ret = 0
        for k in cnt:
            if cnt[k] == 0:
                continue
            ret += 1
            cnt[k] -= 1
            ret += self.dfs(cnt)
            cnt[k] += 1
        return ret

tiles = "AAABBC"
r = Solution()
ans = r.numTilePossibilities(tiles)
print(ans)

        