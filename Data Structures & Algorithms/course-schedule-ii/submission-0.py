class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)
        order = []
        visiting, visited = set(), set()

        for course, pre in prerequisites:
            prereq[course].append(pre)

        # course has 3 possible states
            # visited: added to output
            # visiting: added to cycle
            # unvisited: not added to any

        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True
            
            visiting.add(course)
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            visited.add(course)
            order.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []

        return order
                
