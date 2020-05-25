class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.ans = 0
        for i in range(len(needs)):
            self.ans += price[i] * needs[i]
        self.dfs(price, special, needs, 0)
        return self.ans

    def dfs(self, price, special, needs, cost):
        if cost >= self.ans:
            return
        if max(needs) <= 0:
            self.ans = min(self.ans, cost)
            return
        # new = needs[:]
        for s in special:
            new = needs[:]
            flag = False
            for i in range(len(s) - 1):
                new[i] -= s[i]
                if new[i] < 0:
                    flag = True
                    break
            if not flag:
                self.dfs(price, special, new, cost + s[-1])
        tmp = cost
        for i in range(len(needs)):
            if needs[i] > 0:
                tmp += needs[i] * price[i]
        self.ans = min(self.ans, tmp)