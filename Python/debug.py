class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    cnt = 0
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'int':
        res = []
        self.travel(root, res, sum)
        return self.cnt
    def travel(self, root, res, sum):
        if (root == None):
            return 
        for i in range(len(res)):
            res[i] += root.val
            if res[i] == sum:
                self.cnt += 1
        res.append(root.val)
        if (root.val == sum):
            self.cnt += 1
        if root.left:
            self.travel(root.left, res[:], sum)
        if root.right:
            self.travel(root.right, res[:], sum)

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line);
            line = next(lines)
            sum = int(line);
            
            ret = Solution().pathSum(root, sum)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()