class Solution:
    def nextGreatestLetter(self, letters, target):
        if ord(target) >= ord(letters[-1]):
            return letters[0]
        l = 0
        r = len(letters) - 1
        while l <= r:
            mid = l + (r - l) // 2 
            if ord(letters[mid]) > ord(target) and (mid -1 < 0 or ord(letters[mid - 1]) <= ord(target)):
                return letters[mid]
            if ord(letters[mid]) > ord(target):
                r = mid - 1
            else:
                l = mid + 1        
letters =  ["c", "f", "j"]

tar = "a"
res = Solution()
ans = res.nextGreatestLetter(letters, tar) 
print(ans)