class Solution:
    def reachNumber(self, target: 'int') -> 'int':
        i = 0
        m = 0
        if (target < 0):
            target = -target
        while(m != target):
            i += 1
            if (m + i > target):
                m -= i  
            else:
                m += i
        return i

if __name__ == "__main__":
    res = Solution()
    for i in range(10):
        ans = res.reachNumber(i)
        print(ans)