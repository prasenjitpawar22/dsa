import collections
''' 
Undirected graph cycle detection we use - parent - to check if not coming from the same prev vertex.
'''
class Solution:
    def isCycle(self, V, edges):
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(v, parent):
            visited.add(v)
            for nei in adj[v]:
                # not visited and dfs check
                if nei not in visited and dfs(nei, v):
                        return True
                # visited and coming from parent
                elif nei != parent:
                    return True
            return False

        for i in range(V):
            if i not in visited:
                if dfs(i, -1):
                    return True
        return False
