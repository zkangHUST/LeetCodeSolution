# 官方解法，关键在于产生last字典，保存每个字符最后出现的位置
class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans
res = Solution()
S= "ababcbacadefegdehijhklij"
ans = res.partitionLabels(S)
print(ans)