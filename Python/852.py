class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        flag = 0
        for i in range(1,len(A)):
            
            if ((flag == 0) and A[i]>A[i-1]): 
                continue
            elif ((flag == 0) and A[i]<A[i-1]):        
                flag = 1
                res = i-1
            elif(flag == 1 and A[i] <A[i-1]):
                continue
            elif(flag == 1 and A[i]> A[i-1]):
                return -1
            else:
                return -1
        return res
ans = Solution()
A= [0,2,1,0]
res = ans.peakIndexInMountainArray(A)
print(res)


        