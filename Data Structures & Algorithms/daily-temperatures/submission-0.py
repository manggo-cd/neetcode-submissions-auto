class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we want to have a stack that holds the current most so far
        # we want to pop when we see a value thats greater than the first in our stack
        #   this way we are always evaluating every number 
        # we want to append i - index of first to index of first in a result

        if not temperatures:
            return []

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, ind = stack.pop()
                res[ind] = i - ind
            stack.append((t, i))

        return res


        