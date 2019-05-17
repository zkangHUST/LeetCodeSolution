class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        i = j = 0
        cnt = 0
        len1 = len(nums1)
        len2 = len(nums2)
        if (len1 and len2):
            res = nums1[0] if nums1[0] < nums2[0] else nums2[0]
        elif(len1):
            res = nums1[0]
        elif(len2):
            res = nums2[0]
        cnt = 0
        latch  = 0
        while(i < len1 and j < len2):
            latch = res
            if (nums1[i] <= nums2[j]):
                res = nums1[i]
                i += 1
            elif(nums2[j] < nums1[i]):
                res = nums2[j]
                j += 1
            cnt += 1
            if ((len1 + len2) % 2 == 0):
                if (cnt == (len1 + len2) / 2 + 1):
                    return (res + latch) / 2
            elif (cnt >= (len1 + len2) / 2):
                return res
        while (i < len1):
            latch = res
            res = nums1[i]
            i += 1
            cnt += 1
            if ((len1 + len2) % 2 == 0):
                if (cnt == (len1 + len2) / 2 + 1):
                    return (res + latch) / 2
            elif (cnt >= (len1 + len2) / 2):
                return res
        while (j < len2):
            latch = res
            res = nums2[j]
            j += 1
            cnt += 1
            if ((len1 + len2) % 2 == 0):
                if (cnt == (len1 + len2) / 2 + 1):
                    return (res + latch) / 2
            elif (cnt >= (len1 + len2) / 2):
                return res

res = Solution()
nums1 = [1, 2]  #[1, 3, 4]
nums2 = [1, 2]
ans = res.findMedianSortedArrays(nums1, nums2)
print(ans)