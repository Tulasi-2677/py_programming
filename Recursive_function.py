# Recursion is a programming technique where a function calls itself to solve a problem

def countdown(n):
    if n == 0: # Base case
        return 1
    print(n)
    countdown(n - 1) # Recursive function call

countdown(5)    