class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        i = 0
        j = len(s) - 1
        while(i < j):
            while( i < j and self.check(s[i]) == False):
                i += 1 
            while(i < j and self.check(s[j]) == False):
                j -= 1
            if (s[i] != s[j]):
                return False
            i += 1
            j -= 1
        return True
    def check(self, s):
        if ( (ord(s) >= ord('0') and ord(s) <= ord('9')) or
            (ord(s) >= ord('A') and ord(s) <= ord('Z'))
           ):
            return True
        return False

res = Solution()
while True:
    src = input()
    ans = res.isPalindrome(src)
    print(ans)
