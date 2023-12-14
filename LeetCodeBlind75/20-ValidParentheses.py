
def isValid(s):
    stack = []
    isValid = False
    valid = { ')':'(', ']':'[', '}':'{'}
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        
        elif len(stack) > 0 and stack.pop()==valid[i]:
            isValid = True
        else:
            return False
    return False if len(stack) > 0 else isValid
            
            
print(isValid('()'))
print(isValid('()[]{}'))
print(isValid('(]'))
print(isValid('(){}}{'))
print(isValid('({{{{}}}))'))
print(isValid('([]){'))
print(isValid('){'))

