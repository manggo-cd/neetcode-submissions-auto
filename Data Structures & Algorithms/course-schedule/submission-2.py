class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = defaultdict(list)
        for crs, pre in prerequisites:
            map[crs].append(pre)
        
        taken = set()

        def dfs(course):
            if not map[course]:
                return True

            if course in taken:
                return False
            
            taken.add(course)

            for p in map[course]:
                if not dfs(p):
                    return False

            map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True