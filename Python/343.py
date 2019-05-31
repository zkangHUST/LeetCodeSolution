class Solution:
    def integerBreak(self, n):
        if (n == 2):
            return 1
        if (n == 3):
            return 2
        size = n // 3
        ans = n % 3
        if (ans == 1):
            size -= 1
            ans = 4
        elif ans == 0:
            ans = 1
        while(size > 0):
            ans *= 3
            size -= 1
        return ans

if __name__ == "__main__":
    res = Solution()
    while(True):
        i = int(input())
        if (i == 0):
            break
        print(res.integerBreak(i))

