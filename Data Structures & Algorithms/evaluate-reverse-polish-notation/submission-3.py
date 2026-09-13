class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize stack
        stack = []

        for t in tokens:
            if t == '+':
                n1 = stack.pop()
                n2 = stack.pop()
                num = n2 + n1
                stack.append(num)
                print(num)
            elif t == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                num = n2 - n1
                stack.append(num)
                print(num)
            elif t == '*':
                n1 = stack.pop()
                n2 = stack.pop()
                num = n2 * n1
                stack.append(num)
                print(num)
            elif t == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                num = int(n2 / n1)
                stack.append(num)
                print(num)
            else:
                stack.append(int(t))
        
        return stack[0]