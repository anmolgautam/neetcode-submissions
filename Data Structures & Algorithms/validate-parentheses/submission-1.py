class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappers = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for bracket in s:
            if bracket in mappers:
                if len(stack)>0 and stack[-1] == mappers[bracket]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(bracket)
        return True if len(stack) ==0 else False


        