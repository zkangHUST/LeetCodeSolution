class Solution:
    def rotatedDigits(self, N):
        cnt = 0
        for i in range(N + 1):
            if self.check(i):
                # print(i, end = ", ")
                cnt += 1
        return cnt
    def check(self, n):
        s = list(str(n))
        if (s.count('3') or s.count('4') or s.count('7')):
            return False
        for i in range(len(s)):
            if s[i] in [0,1,8]:
                continue
            if s[i] == '2':
                s[i] = '5'
            elif s[i] == '5':
                s[i] = '2'
            elif s[i] == '6':
                s[i] = '9'
            elif s[i] == '9':
                s[i] = '6'
        s = int(''.join(s))
        if s != n:
            return True
        return False

if __name__ == "__main__":
    res = Solution()
    print(res.rotatedDigits(10))



