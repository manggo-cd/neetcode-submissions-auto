class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbors = defaultdict(list)

        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

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
