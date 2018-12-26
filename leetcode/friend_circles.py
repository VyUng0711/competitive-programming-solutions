# https://leetcode.com/problems/friend-circles/


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # graph = []
        # for i in range(len(M)):
        #     for j in range(len(M[0])):
        #         if M[i][j] == 1:
        #             graph[i] = j
                    
        ranks = [0] * len(M)
        parent = [i for i in range(len(M))]
        
        def findSet(u):
            if parent[u] != u:
                parent[u] = findSet(parent[u])
            return parent[u]
        
        def unionSet(u, v):
            up = findSet(u)
            vp = findSet(v)
            if up == vp:
                return
            if ranks[up] > ranks[vp]:
                parent[vp] = up
            elif ranks[up] < ranks[vp]:
                parent[up] = vp
            else:
                parent[up] = vp
                ranks[vp] += 1
                
        
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    unionSet(i, j)
                    
        count = 0           
        for i in range(len(parent)):
            if parent[i] == i:
                count += 1
        return count
                
                
