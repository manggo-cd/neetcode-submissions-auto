class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairings = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in pairings.values():
                stack.append(c)
            elif c in pairings.keys():
                if stack and stack[-1] == pairings[c]:
                    stack.pop()
                else:
                    return False

        return not stack

