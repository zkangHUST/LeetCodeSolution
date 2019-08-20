class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        x1, y1 = self.convert(a)
        x2, y2 = self.convert(b)
        m = x1 * x2 - y1 * y2
        n = x1 * y2 + x2 * y1
        res = ""
        res += str(m) + "+" + str(n) +"i"
        return res
    def convert(self, a):
        s = a.split("+", 1)
        m = int(s[0])
        s = s[1].split('i', 1)
        n = int(s[0])
        return m , n