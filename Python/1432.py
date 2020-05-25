class Solution:
    def maxDiff(self, num: int) -> int:
        bits = []
        m, n = num, num
        while num:
            bits.append(num % 10)
            num = num // 10
        if not bits:
            return -1
        bits = bits[::-1]
        for i in range(len(bits)):
            if bits[i] < 9:
                m = self.getNum(bits, bits[i], 9)
                break
        
        if bits[0] != 1:
            n = self.getNum(bits, bits[0], 1)
        else:
            for i in range(1, len(bits)):
                if bits[i] > 0 and bits[i] != bits[0]:
                    n = self.getNum(bits, bits[i], 0)
                    break
        print(m, n)
        return m - n
    def getNum(self, bits, m, n):
        ans = 0
        for v in bits:
            ans *= 10
            if v == m:
                ans += n
            else:
                ans += v
        return ans 