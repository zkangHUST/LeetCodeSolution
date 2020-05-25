class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        j = i = max(len(v1), len(v2))

        for c in v1:
            a = int(c) * 10 ** i
            i -= 1
        for c in v2:
            b = int(c) * 10 ** j
            j -= 1
        if a > b:
            return 1
        elif a < b:
            return -1
        return 0

