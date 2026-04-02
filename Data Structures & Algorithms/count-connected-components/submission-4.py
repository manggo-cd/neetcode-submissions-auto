class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0

        # we run DFS on undirected graph to reach the deepest nodes. every time we run DFS we increment our count by 1.
        # during our search, we can add to a set to indicate we've seen this node so far. 
        # essentially each new call stack on a node not in the seen list results in count + 1
        # create adjacency list

        neighbors = defaultdict(list)
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

        seen = set()

        def dfs(node):
            if node in seen:
                return

            seen.add(node)

            for nei in neighbors[node]:
                dfs(nei)

        
        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)

        return count
            
