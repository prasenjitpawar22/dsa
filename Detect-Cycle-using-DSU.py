'''
Function to detect cycle using DSU in an undirected graph.
'''
class Solution:
	def detectCycle(self, V, adj):
	parent = [v for v in range(V)]
	# find with path compression 
	def find(x):
		if parent[x] != x:
			parent[x] = find(parent[x])
        return parent[x]
		
	# without using rank
	def union(x, y):
		x_parent = find(x)
		y_parent = find(y)
		if x_parent != y_parent:
			parent[x_parent] = y_parent
		
	for v in range(V):
		for u in adj[v]:
			if u < v:
				u_p = find(u)
				v_p = find(v)
				if u_p == v_p:
					return 1
				union(u, v)
		
	return 0
