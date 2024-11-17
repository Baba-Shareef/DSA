# Take the user input
Exp = input("Enter the prefix expression:")
#in prefix start from right to left so i change the length to minus
length = -len(Exp) + -1
# Take the empty stack to insert the elements
stack = []
# The iteration start from right o left
for i in range(-1,length,-1):
    # if it is not operator then in push to stack
    if Exp[i] not in ("+","-","*","/"):
        stack.append(Exp[i])
    # if it is operator then take top two elements from stack add operator betwwen operands and then insert into stack
    else:
        str = "(" + stack.pop() + Exp[i] + stack.pop() + ")"
        stack.append(str)
# then return the top stack
print(stack[-1])


