import collections
'''
for cycle detection we use Kahn's algo based on topological sort
'''
class Solution:
    def isCycle(self, V, edges):
        adj = collections.defaultdict(list)
        indegree = [0 for _ in range(V)] 
        
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
         
        # fill up the que
        que = collections.deque()
        for i, d in enumerate(indegree):
            if d == 0:
                que.append(i)

        count = 0
        while que:
            u = que.popleft()
            count += 1
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    que.append(v)
        
        return count != V 
