class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        if len(s) < 10:
            return ans
        tmp = s[0:10]
        p = 10
        cnt = {tmp:1}
        while p < len(s):
            tmp = tmp[1:]
            tmp += s[p]
            p += 1
            if tmp not in cnt:
                cnt[tmp] = 1
            else:
                cnt[tmp] += 1
        for c in cnt:
            if cnt[c] > 1:
                ans.append(c)
        return ans