class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)

        for c,p in prerequisites:
            prereqs[c].append(p)

        seen = set()

        def dfs(course):
            if not prereqs[course]:
                return True

            if course in seen:
                return False

            seen.add(course)

            for p in prereqs[course]:
                if not dfs(p):
                    return False
            prereqs[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True