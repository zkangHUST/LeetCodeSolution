class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        left = 0
        right = 0
        stack = []
        for c in S:
            if c == '(':
                stack.append(c)
                left += 1
            else:
                if len(stack) > 0 and stack[-1] == '(':
                    left -= 1
                    stack.pop()
                else:
                    right += 1
                    stack.append(c)
        return left + right

        