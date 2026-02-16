import math

def is_number(n):
    try:
        float(n) # Type-casting the string to ‘float‘.
    except ValueError:
        return False
    return True

def  interactive_activation_function():
    print("Input x = ")
    x = input()
    if not is_number(x):
        print("x must be a number")
        return
    print("Input activation Function (sigmoid|relu|elu): ")
    f = input()
    if f != "sigmoid" and f != "relu" and f != "elu":
        print(f"{f} is not supportted")
        return

    x = float(x)
    if f == "sigmoid":
        output = 1 / (1 + math.e**(-x))
        print(f"{f}: f({x}) = {output}")
    elif f == "relu":
        output = max(0, x)
        print(f"{f}: f({x}) = {output}")
    else:
        output = 0
        if x <= 0:
            output = 0.01*(math.e**x - 1)
        else: 
            output = x
        print(f"{f}: f({x}) = {output}")
        