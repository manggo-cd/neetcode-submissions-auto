class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # initialize our window 
        # check if window is permutation
        # update window and check
        # if so return true
        # if not return false

        if len(s1) > len(s2):
            return False

        countS1, countS2 = {}, {}

        for i in range(len(s1)):
            countS1[s1[i]] = 1 + countS1.get(s1[i], 0)
            countS2[s2[i]] = 1 + countS2.get(s2[i], 0)

        if countS1 == countS2:
            return True
        
        l = 0

        for i in range(len(s1), len(s2)):
            countS2[s2[i]] = 1 + countS2.get(s2[i], 0)
            countS2[s2[l]] -= 1
            
            if countS2[s2[l]] == 0:
                del countS2[s2[l]]
            l += 1
            if countS1 == countS2:
                return True

        return False


        