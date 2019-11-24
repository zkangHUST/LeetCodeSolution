class Solution:
    def numSmallerByFrequency(self, queries, words) :
        base = sorted([self.f(i) for i in words])
        src = [self.f(i) for i in queries]
        ans = [0 for i in range(len(queries))]
        for i in range(len(queries)):
            for b in base:
                if src[i] >= b:
                    continue
                ans[i]+= 1
        return ans
    def f(self, s):
        m = 'z'
        ans = 0
        for c in s:
            if c <= m:
                ans = s.count(c)
                m = c
        return ans

a = ["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"]
b = ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"]
p = Solution()
ans = p.numSmallerByFrequency(a, b)
print(ans)
