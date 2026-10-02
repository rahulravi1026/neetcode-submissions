class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        info = reversed(sorted((p, s) for p, s in zip(position, speed)))
        stack = []

        for p, s in info:
            time = (target - p) / s
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        
        return len(stack)