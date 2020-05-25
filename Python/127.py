class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        stack = set([beginWord])
        distance = 0
        visited = set([beginWord])
        lookup = set(wordList)
        # print(stack)
        while stack:
            newstack = set()
            for word in stack:
                if word == endWord:
                    return distance + 1
                visited.add(word)
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newword = word[0:i] + c + word[i + 1:]
                        if newword not in visited and newword in lookup:
                            newstack.add(newword)
            distance += 1
            stack = newstack
            # print(stack)
        return 0