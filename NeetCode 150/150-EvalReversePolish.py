class Solution:
    def evalRPN(self, tokens):

        stack = []

        for t in tokens:

            if t == '+':
                stack += [stack.pop() + stack.pop()]
            elif t == '-':
                x,y = stack.pop(),stack.pop()
                stack += [y - x]
            elif t == '*':
                stack += [stack.pop() * stack.pop()]
            elif t == '/':
                x,y = stack.pop(),stack.pop()
                stack += [int(y/x)]
            else:
                stack += [int(t)]
        return stack[0]
        
tokens = ["2","1","+","3","*"]
print(Solution().evalRPN(tokens))