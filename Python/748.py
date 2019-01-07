class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        dic = {}
        res = []
        l = licensePlate.lower()
        for v in l:
            if not v.isalpha():
                continue
            if v not in dic.keys():
                dic[v] = 1
            else:
                dic[v] += 1
        for k in words:
            tmp = self.check(k, dic)
            if (tmp):
                res.append(tmp)
        if not res:
            return None
        tmp = res[0]
        for k in res:
            if len(k) < len(tmp):
                tmp = k
        return tmp
    def check(self, word, dic):
        for key in dic:
            if word.count(key) < dic[key]:
                return None
        return word

res = Solution()
licensePlate = "GrC8950"
words = ["measure","other","every","base","according","level","meeting","none","marriage","rest"]
l = res.shortestCompletingWord(licensePlate, words)
print(l)
