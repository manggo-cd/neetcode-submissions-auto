class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort by taking the array frequency. Array size 26 for each letter, and words that are anagrams will have the same key

        groupings = defaultdict(list)
        res = []

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            groupings[tuple(freq)].append(s)

        for group in groupings.values():
            res.append(group)

        return res