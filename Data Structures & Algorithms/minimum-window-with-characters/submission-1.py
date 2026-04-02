class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window, countT = defaultdict(int), Counter(t)

        need = len(countT)
        have = 0
        minLen = math.inf
        substr = [-1, -1]

        l = 0
        for r,c in enumerate(s):
            window[c] += 1
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                currLen = r - l + 1
                if currLen < minLen:
                    minLen = currLen
                    substr = [l, r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = substr
        return s[l:r + 1] if minLen != math.inf else ""