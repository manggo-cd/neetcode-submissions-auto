class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window approach
        # with a left and right pointer

        # Use a hashmap to check if that letter is already in window.
        # if is, update left pointer and increment a count
        # if not, keep incrementing the right pointer

        charSet = set()
        l = 0
        rsf = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            rsf = max(rsf, r - l + 1)

        return rsf

