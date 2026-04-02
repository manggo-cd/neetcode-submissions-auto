class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = None
        graph = defaultdict(set)
        
        def dfs(n1, n2):
            if n1 in visited:
                return False

            if n1 == n2:
                return True
            
            visited.add(n1)

            for nei in graph[n1]:
                if dfs(nei, n2):
                    return True

            return False

        for n1, n2 in edges:
            visited = set()
            if dfs(n1, n2):
                res = [n1, n2]
            graph[n1].add(n2)
            graph[n2].add(n1)

        return res


        