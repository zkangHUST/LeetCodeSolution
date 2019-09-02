class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones, reverse = True)
        while len(stones) > 1:
            a = stones[0]
            b = stones[1]
            stones = stones[2:]
            if a != b:
                if not stones:
                    stones.append(a - b)
                elif a - b < stones[-1]:
                    stones.append(a - b)
                else:
                    for i in range(len(stones)):
                        if a - b >= stones[i]:
                            stones.insert(i, a - b)
                            break
            print(stones)
        if not stones:
            return 0
        return stones[0]