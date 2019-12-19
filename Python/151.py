class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        words = []
        while i < len(s):
            while i < len(s) and s[i] == ' ':
                i += 1
            start = i
            while i < len(s) and s[i] != ' ':
                i += 1
            if start < i:
                words.append(s[start:i])

        ans = ""
        for i in range(len(words) - 1, -1, -1):
            ans += words[i]
            if i != 0:
                ans += " "
        return ans

s = Solution()

ss = "hello world! "

ans = s.reverseWords(ss)
print(ans)
    