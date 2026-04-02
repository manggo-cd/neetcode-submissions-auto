class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        counter = 0
        visited = set()

        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in neighbors[node]:
                dfs(nei)

        for node in range(n):
            if node not in visited:
                dfs(node)
                counter += 1

        return counter