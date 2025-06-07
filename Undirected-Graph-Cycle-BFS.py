import collections

class Solution:
    def isCycle(self, V, edges):
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def bfs(start):
            queue = collections.deque()
            queue.append((start, -1))  # (node, parent)
            visited.add(start)

            while queue:
                node, parent = queue.popleft()
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, node))
                    elif neighbor != parent:
                        return True  # Found a back edge → cycle
            return False

        for i in range(V):
            if i not in visited:
                if bfs(i):
                    return True
        return False
