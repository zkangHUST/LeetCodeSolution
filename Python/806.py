class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        temp = 0
        l =[0,0]
        lines = 0
        for val in S:
            temp += widths[ord(val)-ord('a')]
            if (temp > 100):
                lines += 1
                temp = widths[ord(val)-ord('a')]
            elif(temp == 100):
                lines += 1
                temp = 0
        if(temp):
            lines+=1
        l[0] = lines
        l[1] = temp
        return l

widths = [7,5,4,7,10,7,9,4,8,9,6,5,4,2,3,10,9,9,3,7,5,2,9,4,8,9]
S = "zlrovckbgjqofmdzqetflraziyvkvcxzahzuuveypqxmjbwrjvmpdxjuhqyktuwjvmbeswxuznumazgxvitdrzxmqzhaaudztgie"
# S = "bbbcccdddaaa"
res=Solution()
res.numberOfLines(widths, S)

        