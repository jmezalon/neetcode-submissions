class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) % 2 = 1:
        #     return 
        valid = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        stack = []

        for ch in s:
            if ch not in valid:
                stack.append(ch)
            else:
                if stack and stack[-1] == valid[ch]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0