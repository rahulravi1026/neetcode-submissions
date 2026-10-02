class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result = [0] * len(temperatures)
        # stack = []

        # for i, temp in enumerate(temperatures):
        #     while stack and temp > stack[-1][1]:
        #         stackI, stackTemp = stack.pop()
        #         result[stackI] = i - stackI
        #     stack.append((i, temp))
        
        # return result

        n = len(temperatures)
        result = [0] * n # result[i] is the next warmer day from day i
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
                elif result[j] == 0:
                    break
                else:
                    j += result[j]
        return result
