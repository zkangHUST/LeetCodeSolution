class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        l = []
        for v in S:
            if (v == '('):
                l.append('(')
            else:
                v = l.pop()
                if (v == '('):
                    l.append(1)
                else:
                    score = 0
                    while (v != '('):
                        score += v
                        v = l.pop()
                    l.append(score * 2)
        return sum(l)
# class Solution(object):
#     def scoreOfParentheses(self, S):
#         stack = [0]
#         for par in S:
#             if par == "(": stack.append(0)
#             else:
#                 last = stack.pop()
#                 if last == 0: score = 1
#                 else: score = last * 2
#                 stack[-1] += score
#         return stack[0]
res = Solution()
S="()(()()(()))"
ans = res.scoreOfParentheses(S)
print(ans)