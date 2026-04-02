class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        for crs,pre in prerequisites:
            prereqs[crs].append(pre)
        
        taken = set()

        def dfs(course):
            if not prereqs[course]:
                return True

            if course in taken:
                return False

            taken.add(course)

            for p in prereqs[course]:
                if not dfs(p):
                    return False
                
            prereqs[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True


            

            