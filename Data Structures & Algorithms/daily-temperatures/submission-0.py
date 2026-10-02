class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackI, stackTemp = stack.pop()
                result[stackI] = i - stackI
            stack.append((i, temp))
        
        return result