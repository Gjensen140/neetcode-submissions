class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []
        stack = []
        opening = 0
        closing = 0


        def expand(opening, closing):
            if len(stack) > (2*n):
                return
            if closing == n and closing == opening:
                output.append("".join(stack))
                return
            

            if opening < n:
                stack.append("(")
                expand(opening + 1, closing)
                stack.pop()


            if opening > closing and closing < n:
                stack.append(")")
                expand(opening, closing + 1)
                stack.pop()

        expand(opening, closing)
        return output
