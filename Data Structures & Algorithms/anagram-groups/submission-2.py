class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # keeps track of occurences

            for c in s:
                count[ord(c) - ord("a")] += 1 # ord gives unicode number
        
            res[tuple(count)].append(s) # maps the character to the count

        return list(res.values())