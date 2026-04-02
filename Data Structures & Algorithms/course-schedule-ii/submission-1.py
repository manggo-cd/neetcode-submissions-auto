class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        prereqs = defaultdict(list)
        for crs,pre in prerequisites:
            prereqs[crs].append(pre)

        visiting, visited = set(), set()

        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)
            for p in prereqs[course]:
                if not dfs(p):
                    return False

            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res
