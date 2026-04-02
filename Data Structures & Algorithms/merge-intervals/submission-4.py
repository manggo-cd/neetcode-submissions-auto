class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            [[]]
        
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]

        for s,e in intervals[1:]:
            prevStart, prevEnd = res[-1][0], res[-1][1]

            if s <= prevEnd:
                res[-1][0] = min(prevStart, s)
                res[-1][1] = max(prevEnd, e)
            else:
                res.append([s, e])

        return res