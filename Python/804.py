morescode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ans = set()
        for val in words:
            res = self.convert(val)
            if res not in ans:
                ans.add(res)
        return len(ans)

    def convert(self, word):
        res = ""
        for val in word:
            res += morescode[ord(val)-ord('a')]
        return res 
res = Solution()
words = ["gin", "zen", "gig", "msg"]
ans = res.uniqueMorseRepresentations(words)
