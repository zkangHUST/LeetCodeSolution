import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        nums = [1]
        visited = {1}
        for i in range(1, n):
            top = heapq.heappop(nums)
            for k in primes:
                if top * k not in visited:
                    heapq.heappush(nums, top * k)
                    visited.add(top * k)
        return heapq.heappop(nums)

