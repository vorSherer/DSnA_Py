# Your function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets:

# Round Brackets : ()
# Square Brackets : []
# Curly Brackets : {}


def multi_bracket_validation(input):
    """
    docstring here.
    """
    stack = []

    for elem in input:
        if elem in ["(", "[", "{"]:
            stack.append(elem)
        else:
            if elem == ")" and stack[-1] == "(":
                stack.pop
            elif elem == "]" and stack[-1] == "[":
                stack.pop
            elif elem == "}" and stack[-1] == "{":
                stack.pop

    if stack:
        return False

    return True






if __name__ == "__main__":
    str1 = "{{[()]}}"
    if multi_bracket_validation(str1):
        print("String is balanced.")
    else:
        print("String is not balanced.")
        

