class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbors = defaultdict(list)
        for node, nei in edges:
            neighbors[node].append(nei)
            neighbors[nei].append(node)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for nei in neighbors[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n

