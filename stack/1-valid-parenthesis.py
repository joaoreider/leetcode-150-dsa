class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_type = [")", "]", "}"]
        char_map = {
            "}": "{",
            ")": "(",
            "]": "[",
        }

        for c in s:
            if c in closing_type:
                if len(stack) == 0:
                    return False 
                stack_top = stack[-1]
                closing_opener = char_map[c] 
                if closing_opener == stack_top:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        return False

#s = "([{}])"
print(Solution().isValid("([{}])"))
print(Solution().isValid("()))"))
print(Solution().isValid("([["))
print(Solution().isValid("[(])"))
print(Solution().isValid("[]"))

