class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        res = []

        for x, y in points:
            dist = -((x ** 2) + (y **2))
            heapq.heappush(q, [dist, x, y])

            if len(q) > k:
                heapq.heappop(q)

        while q:
            dist, x, y = heapq.heappop(q)
            res.append([x, y])

        return res