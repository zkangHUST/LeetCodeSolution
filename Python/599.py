class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        len1 = len(list1)
        len2 = len(list2)
        minsum = len1 + len2
        res = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if (list1[i] == list2[j]):
                    tmp = i + j
                    if tmp < minsum:
                        minsum = tmp
                        res.clear()
                        res.append(list1[i])
                    elif tmp == minsum:
                        res.append(list1[i])
        return res