def isValid(s):
    if len(s) == 1: return False
    close_info = {'}':'{', ')':'(', ']':'['}
    stack = []
    for c in s:
        if c in close_info.values():
            stack.append(c)
        else:
            if not stack or stack.pop() != close_info[c]:
                return False
    if len(stack) != 0:
        return False
    return True

print(isValid("([{}])"))
print(isValid("[(])"))