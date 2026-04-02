class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # simply walk the string and check if the next element is 1 bigger than the previous seen element
        # return the len of our list
        numSet = set(nums)
        res = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                res = max(res, length)

        return res

