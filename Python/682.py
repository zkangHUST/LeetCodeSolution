class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        score=[]
        for key in ops:
            if(self.isscore(key)):
                score.append(int(key))
            elif(key=='C' and score):
                score.pop()
            elif(key=='D'):
                n = score[-1]*2
                score.append(n)
            elif(key=='+'):
                n = score[-1]+score[-2]
                score.append(n)
        return sum(score)
    def isscore(self,score):
        if(score.isdigit()):
            return int(score)
        elif(score[0]=='-' and score[1:].isdigit()):
            return -1*int(score[1:])
        else:
            return 0
res = Solution()
ops=["5","-2","4","C","D","9","+","+"]
print(res.calPoints(ops))