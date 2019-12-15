class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = {}
        for num in arr:
            if num not in cnt:
                cnt[num] = 1
            else:
                cnt[num] += 1
        cnt2 = {}

        for key, val in cnt.items():
            if val not in cnt2:
                cnt2[val] = 1
            else:
                return False
        return True

