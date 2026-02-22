def factorial_function(n):
    if n < 0:
        return
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output

def approx_sin(x, n):
    sin_approx = 0
    for i in range(0, n + 1):
        index = (-1)**i
        tu_so = x**(2*i + 1)
        mau_so = factorial_function(2*i + 1)
        sin_approx += index*(tu_so/mau_so)
    return sin_approx

def approx_cos(x, n):
    cos_approx = 0
    for i in range(0, n + 1):
        index = (-1)**i
        tu_so = x**(2*i)
        mau_so = factorial_function(2*i)
        cos_approx += index*(tu_so/mau_so)
    return cos_approx

def approx_sinh(x, n):
    sinh_approx = 0
    for i in range(0, n + 1):
        tu_so = x**(2*i + 1)
        mau_so = factorial_function(2*i + 1)
        sinh_approx += (tu_so/mau_so)
    return sinh_approx

def approx_cosh(x, n):
    cosh_approx = 0
    for i in range(0, n + 1):
        tu_so = x**(2*i)
        mau_so = factorial_function(2*i)
        cosh_approx += (tu_so/mau_so)
    return cosh_approx


print(approx_sin(3.14, 10))
print(approx_cos(3.14, 10))
print(approx_sinh(3.14, 10))
print(approx_cosh(3.14, 10))