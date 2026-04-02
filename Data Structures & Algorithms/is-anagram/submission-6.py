class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq, tFreq = Counter(s), Counter(t)
        return sFreq == tFreq
        