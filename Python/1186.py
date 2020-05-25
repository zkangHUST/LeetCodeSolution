class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if not arr:
            return 0
        dp1 = [0 for i in range(len(arr))]
        dp2 = dp1[:]
        dp1[0] = arr[0]
        dp2[0] = min(0, arr[0])
        ans = dp2[0]
        for i in range(1, len(arr)):
            dp1[i] = max(arr[i], dp1[i - 1] + arr[i])
            dp2[i] = max(dp1[i - 1], dp2[i - 1] + arr[i])
            ans = max(dp1[i], dp2[i], ans)
        return ans