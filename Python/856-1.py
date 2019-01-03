class Solution(object):
    def scoreOfParentheses(self, S):
        stack = [0]
        for par in S:
            if par == "(": stack.append(0)
            else:
                last = stack.pop()
                if last == 0: score = 1
                else: score = last * 2
                stack[-1] += score
        return stack[0]
res = Solution()
S="()(()()(()))"
ans = res.scoreOfParentheses(S)
print(ans)