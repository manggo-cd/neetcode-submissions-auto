class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # for any given subsequence, we want to find some anchor points. 
        # anchor points start where there exists an element, and there is
        # no element that is element - 1 in our array. 
        #.     this is because, we would just be counting a permutation 


        numSet = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in numSet:
                currLength = 1
                while n + 1 in numSet:
                    currLength += 1
                    n += 1
                longest = max(longest, currLength)

        return longest