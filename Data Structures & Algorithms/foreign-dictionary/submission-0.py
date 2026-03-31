class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {char: set() for word in words for char in word}

        for i in range(1, len(words)):
            word1, word2 = words[i - 1], words[i]
            minLen = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            
            for j in range(minLen):
                if word1[j] != word2[j]:
                    adjList[word1[j]].add(word2[j])
                    break
            
        res = []
        visited = {}
        
        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for nei in adjList[char]:
                if dfs(nei):
                    return True
            
            visited[char] = False

            res.append(char)
        
        for char in adjList:
            if dfs(char):
                return ""
        
        return "".join(list(reversed(res)))