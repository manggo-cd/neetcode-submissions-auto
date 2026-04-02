class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS, counterT = Counter(s), Counter(t)
        return counterS == counterT
        