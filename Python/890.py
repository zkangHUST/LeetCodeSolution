# 掌握字典的访问方法
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        l =[]
        for v in words:
            if self.check(v, pattern):
                l.append(v)
        return l
    def check(self, word,pattern):
        if (len(word) != len(pattern)):
            return False
        dir = {}
        for m,n in zip(pattern,word):
            if m not in  dir:
                if n in dir.values():
                    return False
                dir[m] = n
            else:
                if dir[m] != n:
                    return False
        return True

words = ["ccc","deq","mee","aqq","dkd","abc"]
pattern = "abb"
res = Solution()
ans = res.findAndReplacePattern(words,pattern)
print(ans)

