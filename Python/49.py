class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        dic = {}
        for s in strs:
            k = "".join(sorted(s))
            if k not in dic:
                dic[k] = [s]
            else:
                dic[k].append(s)
        for k in dic:
            ans.append(dic[k])
        return ans