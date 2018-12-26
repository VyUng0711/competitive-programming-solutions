# https://leetcode.com/problems/course-schedule/

# Solution using BFS:

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[u].append(v)
            
        print(graph)
        def find_one_loop(start, graph, numCourses):
            stack = [start]
            visited = [False] * numCourses
            while stack:
                top = stack.pop()
                for neighbor in graph[top]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
                        if neighbor == start:
                            return True
            return False
        
        for i in range(numCourses):
            cur = find_one_loop(i, graph, numCourses)
            print(cur)
            if cur:
                return False
        return True

# Solution using DFS - topological sort:

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] * numCourses for _ in range(numCourses)]
        status = {}
        for u, v in prerequisites:
            graph[u].append(v)
            status[u] = 0
            status[v] = 0
        for i in status.keys():
            # Don't explore if already visited 
            if status[i] == 2:
                continue
                
            stack = [i]
            while stack:
                top = stack[-1]
                if status[top] == 1:
                    status[top] = 2
                    stack.pop()
                    continue
                status[top] = 1
                for neighbor in graph[top]:
                    # If neighbor is visited, do nothing
                    if status[neighbor] == 2:
                        continue
                    # If neighbor is still in visiting status, there exists a cycle
                    if status[neighbor] == 1:
                        return False
                    # If neighbor is not visited, add neighbor to stack.
                    stack.append(neighbor)
        return True

            
