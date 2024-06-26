def revers_string(s):
    string = list(s)
    reversed = ''
    for i in string:
        reversed = i + reversed
    print(reversed)
revers_string('Hello')

# using slincing
def reverse(s):
    return s[::-1]
print(reverse('world'))

# using stack 
def rec_stack(s):
    string = list(s)
    revese = ''
    while string:
        revese += string.pop()
    return revese
print(rec_stack('orange'))

# using join
def reverse_string(s):
    # ''.join(s for s in s[::-1])
    return ''.join(reversed(s))
print(reverse_string('one'))


# using recursion
def recursion_string(s):
    if len(s) == 0:
        return ''
    else:
        return recursion_string(s[1:]) + s[0]
print(recursion_string('night'))