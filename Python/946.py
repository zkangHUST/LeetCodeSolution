class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        i, j = 0, 0
        while i < len(popped):
            if stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
                continue
            if j < len(pushed):
                if  pushed[j] != popped[i]: 
                    stack.append(pushed[j])  
                else:
                    i += 1 
                j += 1
                continue
            return False
        return True

pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]

p = Solution()
ans = p.validateStackSequences(pushed, popped)
print(ans)
