class Solution:
    def threeSumClosest(self, nums, target):
        i = 0
        Sum = nums[0] + nums[1] + nums[2]
        mindiff = target - Sum  
        size = len(nums)
        nums.sort()
        res = Sum
        while(i < size):
            j = i + 1
            k = size - 1
            # target - nums[i]
            while(j < k):
                Sum = nums[i] + nums[j] + nums[k]
                tmp = target - Sum
                if (abs(tmp) < abs(mindiff)):
                    mindiff = tmp
                    res = Sum
                if (tmp < 0):
                    k -= 1
                elif (tmp > 0):
                    j += 1
                else:
                    return Sum
            i += 1
        return res

if __name__ == "__main__":
    res = Solution()
    nums = [0,1,2]
    result = res.threeSumClosest(nums, 0)
    print(result)


        