class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        daysCount = [0]*len(temperatures)

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                daysCount[stackI] = i - stackI
            stack.append((t,i))

        return daysCount