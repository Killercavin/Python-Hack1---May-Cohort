# Setting the variable s as an input
s = str(input("Enter your string: "))

# function declaration
def reverse_string(s: str) -> str:

    # Empty stack initialization
    stack = []

    # Appending all the characters of the string to the stack by looping
    for i in s:
        stack.append(i)
    
    # Popping all the characters of the string and appending the reversed string
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    
    return f"The reversed string is {reversed_string}"

# Test the function
test_function = reverse_string(s)
print(test_function)