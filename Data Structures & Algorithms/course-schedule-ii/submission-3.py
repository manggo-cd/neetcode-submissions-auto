class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)
        res = []

        for c,p in prerequisites:
            prereqs[c].append(p)

        visiting, visited = set(), set()

        def dfs(course):
            if course in visited:
                return True

            if course in visiting:
                return False

            visiting.add(course)
            for nei in prereqs[course]:
                if not dfs(nei):
                    return False

            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res