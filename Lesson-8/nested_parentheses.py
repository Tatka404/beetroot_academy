def nested_parentheses(incoming):
    stack = []
    bracket = {'(': ')'}

    for char in incoming:
        if char in ['(']:
            stack.append(char)
        else:
            if stack:
                top = stack.pop()
                if bracket[top] != char:
                    return False
            else:
                return False
    return False if stack else True


row_to_check = input('Type down your row to check: ')
print(nested_parentheses(row_to_check))
