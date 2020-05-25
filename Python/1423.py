class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = len(cardPoints) - k
        m = sum(cardPoints)
        a = sum(cardPoints[0:l])
        b = a
        # print(n)
    
        for i in range(l, len(cardPoints)):
            a = a - cardPoints[i - l] + cardPoints[i]
            b = min(b, a)
            # print(b)
            # n = min(n, n - cardPoints[i - k] + cardPoints[i])
            
            # print(n)
        return m - b