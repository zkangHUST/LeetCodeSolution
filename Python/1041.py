class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0, 0, 0, 1]
        instructions = instructions * 4
        for cmd in instructions:
            self.move(pos, cmd)
        return pos[0] == 0 and pos[1] == 0
    def move(self, pos, cmd):
        if cmd == 'G':
            pos[0] += pos[2]
            pos[1] += pos[3]
        elif cmd == 'L':
            pos[2], pos[3] = pos[3] * -1, pos[2] * 1
        elif cmd == 'R':
            pos[2], pos[3] = pos[3] * 1, pos[2] * -1

dir = "LLGRL"
p = Solution()
ans = p.isRobotBounded(dir)
print(ans)