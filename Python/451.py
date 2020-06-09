class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = {}
        for c in s:
            if c not in cnt:
                cnt[c] = 1
            else:
                cnt[c] += 1
        cnt = sorted(cnt.items(), key = lambda item:item[1], reverse = True)
        ret = ""
        for k, v in cnt:
            ret += k * v
        return ret