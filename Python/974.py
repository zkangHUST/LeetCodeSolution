class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        cnt = {0:1}
        s, ans = 0, 0
        for n in A:
            s += n
            k = (s % K + K) % K 
            if k not in cnt:
                cnt[k] = 1
            else:
                ans += cnt[k]
                cnt[k] += 1
        return ans