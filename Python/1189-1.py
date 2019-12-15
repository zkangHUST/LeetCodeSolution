class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = [0] * 128
        for c in text:
            if c in "balloon":
                cnt[ord(c)] += 1
        cnt[ord('l')] = cnt[ord('l')] // 2
        cnt[ord('o')] = cnt[ord('o')] // 2

        mincnt = len(text)
        for c in "balon":
            mincnt = min(mincnt, cnt[ord('c')])
        return mincnt