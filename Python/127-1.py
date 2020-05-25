class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        stack = set(beginWord)
        distance = 0
        visited = {}
        while stack:
            newstack = set()
            for word in stack:
                if word == endWord:
                    return distance + 1
                visited[word] = 1
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newword = word[0:i] + c + word[i + 1:]
                        if newword not in visited and newword in wordList:
                            newstack.add(newword)
            distance += 1
            stack = newstack

        return 0