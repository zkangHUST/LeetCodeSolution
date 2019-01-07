class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        l = {}
        i = 0
        for v in order:
            l[v] = i
            i += 1
        i = 0
        while(i + 1 < len(words)):
            res = self.compare(words[i], words[i+1], l)
            if (res == False):
                return False
            i += 1
        return True
    def compare(self, word1, word2, order):
        i = 0
        while (i < min(len(word1), len(word2))):
            if (order[word1[i]] == order[word2[i]]):
                i += 1
                continue
            elif (order[word1[i]] > order[word2[i]]):
                return False
            else:
                return True     
        if (len(word1) > len(word2)):
            return False
        return True
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
res = Solution()
result = res.isAlienSorted(words, order)
print(result)

        
