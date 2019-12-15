class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        ans = []
        mindiff = 0
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if not ans:
                mindiff = diff
                ans.append([arr[i], arr[i + 1]])
            elif diff > mindiff:
                continue
            else:
                if diff < mindiff:
                    ans.clear()
                ans.append([arr[i], arr[i + 1]])
                mindiff = diff
        return ans