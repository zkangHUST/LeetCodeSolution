class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        tmp = self.fact(n - 1)
        path = ""
        i = 1
        n -= 1
        while k:
            if k > tmp:
                k -= tmp
                i += 1
                while str(i) in path:
                    i += 1
            else:
                path += str(i)
                for val in range(1, 10):
                    if str(val) not in path:
                        i = val
                        break
                if n:
                    tmp = tmp / n
                    n -= 1
                else:
                    break
        return path

    def fact(self, n):
        ans = 1
        while n > 0:
            ans *= n
            n -= 1
        return ans

p = Solution()
print(p.getPermutation(4, 9))