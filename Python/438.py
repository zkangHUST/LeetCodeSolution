class Solution:
    def findAnagrams(self, s, p):
        base = [0 for i in range(26)]
        m = [0 for i in range(26)]
        l = len(p)
        ans = []
        
        for c in p:
            base[ord(c)- ord('a')] += 1

        for i in range(len(s)):
            if i >= l:
                m[ord(s[i - l]) - ord('a')] -= 1
            m[ord(s[i]) - ord('a')] += 1

            if m == base:
                ans.append(i - l + 1)
                
        return ans
s = "cbaebabacd"
p = "abc"

t = Solution()
ans = t.findAnagrams(s, p)

print(ans)