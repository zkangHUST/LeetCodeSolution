class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                tmp = self.check(words[i], words[j])
                if tmp > max:
                    max = tmp
        return max
    def check(self, a, b):
        if len(a) > len(b):
            a , b = b, a
        for c in a:
            if c in b:
                return 0
        return len(a) * len(b)
    
        