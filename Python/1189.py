class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = {}
        for c in "balloon":
            cnt[c] = 0
        for c in text:
            if c in cnt:
                cnt[c] += 1
        cnt['l'] = cnt['l'] // 2
        cnt['o'] = cnt['o'] // 2
        mincnt = len(text)

        for key, val in cnt.items():
            mincnt = min(mincnt, val)
        return mincnt