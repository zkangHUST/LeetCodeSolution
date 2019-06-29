class Solution:
    def deckRevealedIncreasing(self, deck):
        deck = sorted(deck)
        res = [0] * len(deck)
        cnt = 0
        i = 0
        tmp = 2
        while cnt < len(deck):
            while tmp != 2:
                i =  (i + 1) % len(deck)
                if (res[i] == 0):
                    tmp += 1
            res[i] = deck[cnt]
            tmp = 0
            cnt += 1
        return res

deck = [17,13,11,2,3,5,7]

res = Solution()
t = res.deckRevealedIncreasing(deck)
print(t)