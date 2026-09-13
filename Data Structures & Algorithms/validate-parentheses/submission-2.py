class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for c in s:
            # Appending the opening braces
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')' and (len(stack) == 0 or stack.pop() != '('):
                return False
            elif c == ']' and (len(stack) == 0 or stack.pop() != '['):
                return False
            elif c == '}' and (len(stack) == 0 or stack.pop() != '{'):
                return False

        if len(stack) > 0:
            return False
         
        return True