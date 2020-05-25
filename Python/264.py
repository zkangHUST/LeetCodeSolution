import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # import heapq
        nums = [1]
        visited = {1}
        for i in range(1, n):
            top = heapq.heappop(nums)
            for k in [2, 3, 5]:
                if top * k not in visited:
                    heapq.heappush(nums, top * k)
                    visited.add(top * k)
        # heapq.heappush(nums, )
        # print(nums)
        return heapq.heappop(nums)

