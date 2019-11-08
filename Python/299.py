class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull, cows = 0, 0
        cnts = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            if secret[i] in cnts:
                cnts[secret[i]] += 1
            else:
                cnts[secret[i]] = 1
        for c in guess:
            if c in cnts and cnts[c] > 0:
                cnts[c] -= 1
                cows += 1
        ret = ""
        ret = ret + str(bull) + "A" + str(cows - bull) + "B"
        return ret