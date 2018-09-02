class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x=0
        y=0
        for step in moves:
            if(step == 'L'):
                x-=1
            elif(step == 'R'):
                x+=1
            elif(step == 'U'):
                y+=1
            elif(step == 'D'):
                y-=1
        if(x==0 and y == 0):
            return True
        else:
            return False
res = Solution()
res.judgeCircle("LLRRUUDD")
if(res):
    print("true")
else:
    print("false")