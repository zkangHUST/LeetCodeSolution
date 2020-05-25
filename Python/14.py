class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:  
        if not strs:
            return ""
        minlen = len(strs[0])
        for s in strs:
            minlen = min(minlen, len(s))
        for i in range(minlen):
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return s[0:i]
        return strs[0][0:minlen]
