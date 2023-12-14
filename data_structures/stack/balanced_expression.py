stack = []
def checkBalanced(expr):
    for i in expr:
        if i in ["{", "[", "("]:
            stack.append(i)
        elif i in ["}", "]", ")"]:
            if not stack:
                return False
            top = stack.pop()
            if (
                i == "}"
                and top != "{"
                or i == "]"
                and top != "["
                or i == ")"
                and top != "("
            ):
                return False
        else:
            print("Invalid Expression")
            return False

    return not len(stack)

# main function
expr = input()
if not checkBalanced(expr):
    print("Not Balanced")
else:
    print('Balanced')
