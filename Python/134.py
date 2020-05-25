class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            if self.get(gas, cost, i):
                return i
        return -1

    def get(self, gas, cost, i):
        left = gas[i] - cost[i]
        if left < 0:
            return False
        j = (i + 1) % len(gas)
        while True:
            if j == i:
                return True
            left += gas[j]
            left -= cost[j]
            if left < 0:
                return False
            j = (j + 1) % len(gas)
        return True