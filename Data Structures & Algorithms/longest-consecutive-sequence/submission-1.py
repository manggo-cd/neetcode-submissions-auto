class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # walk the array. for each number in the array, check if 1 greater number exists in the array. 
        # if so, continue to add 1 to the length of our consecutive array and collect the longest length
        # each time. 
        # return the len of our list
        
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                    longest = max(longest, length)
        return longest
