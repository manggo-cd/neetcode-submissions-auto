class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        neighbors = defaultdict(list)
        for crs,pre in prerequisites:
            neighbors[crs].append(pre)

        visiting, visited = set(), set()

        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True

            visiting.add(course)
            for nei in neighbors[course]:
                if not dfs(nei):
                    return False

            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res

        