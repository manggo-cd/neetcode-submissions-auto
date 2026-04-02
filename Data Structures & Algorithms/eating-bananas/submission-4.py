class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # for a list of piles, the maximum min eating rate we can get
        # is the max value of the piles (example: if we have [1,4,5,11], 
        # we can essentially say the max bananas per hour is 11 because
        # every other pile can be eaten in 1 hour as well)

        # so, the range would be from 1 banana/hour to max banana in array/hour
        # we can use bin search to determine this and append to a rsf

        l, r = 1, max(piles)
        k = r
       
        while l <= r:
            rate = (l + r) // 2
            
            hours = 0
            for b in piles:
                hours += math.ceil(b / rate)
            
            if hours <= h:
                k = min(k, rate)
                r = rate - 1
            else:
                l = rate + 1

        return k

       



                
                

        