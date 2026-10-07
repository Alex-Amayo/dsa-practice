class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }
        stack = []

        for c in s:
            if c in dict:
                if stack and dict[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if stack == []:
            return True
        else:
            return False