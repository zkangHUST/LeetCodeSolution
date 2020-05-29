class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = {}
        for n in arr:
            if n not in cnt:
                cnt[n] = 1
            else:
                cnt[n] += 1
        ans = float("-inf")
        for k in cnt:
            if cnt[k] == k:
                ans =  max(ans, k)
        if ans == float("-inf"):
            return -1
        return ans 