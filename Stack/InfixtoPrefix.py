def precedence(operator):
    if operator == '^':
        return 3
    elif operator in ("*","/"):
        return 2
    elif operator in ("+","-"):
        return 1
def infixtoprefix(char):
    stack = []
    st = ""
    for i in char:
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') or (i >= '0' and i <= '9'):
            st += i
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                st += stack.pop()
            stack.pop()
        else:
            while stack and (precedence(i) < precedence(stack[-1]) or precedence(i) == precedence(stack[-1])):
                st += stack.pop()
            stack.append(i)
    while stack:
        st += stack.pop()
    return st
demo = infixtoprefix("a+b*c^q")
print(demo)