class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groupings = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord("a")] += 1
            groupings[tuple(key)].append(s)

        for anagrams in groupings.values():
            res.append(anagrams)
        
        return res