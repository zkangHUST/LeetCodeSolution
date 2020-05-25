class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first) - len(second)) > 1 :
            return False
        if len(first) < len(second):
            first, second = second, first
        op = 0
        if len(first) == len(second):
            for i in range(len(first)):
                if first[i] != second[i]:
                    if op >= 1:
                        return False
                    else:
                        op += 1
        else:
            i, j = 0, 0
            while (i < len(first) and j < len(second)):
                if first[i] == second[j]:
                    i += 1
                    j += 1
                else:
                    op += 1
                    if op > 1:
                        return False
                    i += 1
                    if first[i] != second[j]:
                        return False
        return True
