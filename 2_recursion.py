def f(b0, y0, k, x):
        if k == 0:
            return y0
        bk = b0 * (x ** 2)
        b0 = bk

        yk = b0 * y0
        y0 = yk

        k = k - 1
        return f(b0, y0, k, x)

def func(x, k): 
    if x <= 0:
        print("Incorrect value!")
        return
    b0 = 1 / (2 * x)
    y0 = 1

    a = f(b0, y0, k, x)
    return a
    
print(func(1, 3))
