class Solution(object):

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1="qwertyuiop"
        line2="asdfghjkl"
        line3="zxcvbnm"
        ans=[]
        for word in words:
            temp = word.lower()
            if (self.findWord(temp, line1)):
                ans.append(word)
            elif(self.findWord(temp,line2)):
                ans.append(word)
            elif(self.findWord( temp, line3)):
                ans.append(word)
        return ans  
    def findWord(self, word,base):
        for char in word:
            if char not in base:
                return False
        return True            
   
ans = Solution()
words=["Hello", "Alaska", "Dad", "Peace"]
res = ans.findWords(words)
print(res)