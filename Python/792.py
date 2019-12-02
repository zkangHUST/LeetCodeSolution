class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        m = {}
        for i in range(len(S)):
            if S[i] not in m:
                m[S[i]] = [i]
            else:
                m[S[i]].append(i)
        cnt = 0
        wordmap = {}
        for word in words:
            if word not in wordmap:
                wordmap[word] = 1
            else:
                wordmap[word] += 1

        for word in wordmap:
            if self.isMatch(m, word):
                cnt += wordmap[word]
        return cnt

    def isMatch(self, m, word):
        index = -1
        for c in word:
            if c not in m:
                return False
            prev = bisect.bisect_left(m[c], index + 1)
            if prev == len(m[c]):
                return False
            index = m[c][prev]
        return True


    def binarySearch(self, nums, pos):
        l, r = 0, len(nums)
        ans = len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < pos:
                l = l + 1
            else:
                ans = mid 
                r = mid 
        return ans