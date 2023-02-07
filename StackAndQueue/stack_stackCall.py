# the recursion  also use the stack call in the memory 
def fact(c):
    if c == 1:
        return 1
    else:
        return c*fact(c-1)

print(fact(6))