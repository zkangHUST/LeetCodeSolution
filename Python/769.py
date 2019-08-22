class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        self.cnt = 1
        self.split(arr)
        return self.cnt
    def split(self, arr):
        flag = False
        for i in range(1, len(arr)):
            if max(arr[0:i]) < min(arr[i:]):
                self.cnt += 1
                flag = True
                break
        if flag:
            self.split(arr[i:])
        return 