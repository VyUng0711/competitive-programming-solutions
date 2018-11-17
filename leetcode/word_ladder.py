from collections import defaultdict
import queue
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def differ_by_one(a, b):
            diff = 0
            if len(a) != len(b):
                return False
            for i in range(len(a)):
                if a[i] != b[i]:
                    if diff > 0:
                        return False
                    diff += 1
            return diff <= 1
        
        def bfs(start, end):
            q = queue.Queue()
            q.put(start)
            visited[start] = True
            dist[start] = 1
            while not q.empty():
                top = q.get()
                if top == end:
                    return dist[top]
                for neighbor in graph[top]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.put(neighbor)
                        dist[neighbor] = dist[top] + 1
            return 0
        
        wordList.append(beginWord)
        graph = defaultdict(list)
        for i in range(len(wordList) - 1):
            for j in range(i + 1, len(wordList)):
                if differ_by_one(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
                    
        visited = {x: False for x in wordList}
        dist = {x: -float('inf') for x in wordList}
        return bfs(beginWord, endWord)
        
        
        
