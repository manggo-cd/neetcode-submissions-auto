class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        rate = r

        while l <= r:
            currRate = (l + r) // 2
            hours = 0
            for b in piles:
                hours += math.ceil(b / currRate)
            if hours <= h:
                rate = min(rate, currRate)
                r = currRate - 1

            else:
                l = currRate + 1

        return rate

