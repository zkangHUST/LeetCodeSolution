class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        wordList = set(wordList)
        self.path = []
        path = []
        visited = {beginWord}
        self.dfs(visited,wordList, beginWord, path, endWord)
        return self.path
    def dfs(self, visited, wordList, word, path, endWord):
        if word == endWord:
            self.path = path + [endWord]
            return True
        path.append(word)
        visited.add(word)
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                newword = word[:i] + c + word[i + 1:]
                if newword not in wordList or newword in visited:
                    continue
                if newword in wordList and self.dfs(visited, wordList, newword, path[:], endWord):
                    return True
                    
        return False