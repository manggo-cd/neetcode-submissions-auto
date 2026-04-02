class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temps = []

        for i,t in enumerate(temperatures):
            while temps and t > temps[-1][1]:
                idx, tmp = temps.pop()
                res[idx] = i - idx

            else:
                temps.append([i, t])

        return res