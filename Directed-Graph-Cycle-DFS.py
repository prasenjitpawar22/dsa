import collections
'''
for cycle detection in directed graph with DFS we use recursion stack,
to keep track of current visited nodes.
'''
class Solution:
    def isCycle(self, V, edges):
        # dfs
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            
        recursion = set()
        
        def dfs(v):
            if v in recursion:
                return True
                
            recursion.add(v)
            
            for nei in adj[v]:
                if dfs(nei):
                    return True
                    
            recursion.remove(v)

            return False
        
        for n in range(V):
            if dfs(n):
                return True
        
        return False
        
