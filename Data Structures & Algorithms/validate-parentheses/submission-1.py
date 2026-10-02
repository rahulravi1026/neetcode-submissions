class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = { ')' : '(', '}' : '{', ']' : '[' }
        stack = []

        for c in s:
            if c not in bracketMap:
                stack.append(c)
                continue
            if stack and stack[-1] == bracketMap[c]:
                stack.pop()
            else:
                return False
        
        return not stack
