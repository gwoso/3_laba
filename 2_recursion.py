def b_k(b, x, k): 
    if k == 0:
        return b
    bk = b * (x ** 2)
    return bk

def y_k(b, y, k): 
    if k == 0:
        return b
    yk = b * y
    return yk

def func(x, k): 
    if x == 0:
        print("Incorrect value!")
        return
    b0 = 1 / (2 * x)
    y0 = 1

    def f(b0, y0, k):
        if k == 0:
            return y0
        bk = b_k(b0, x, k)
        b0 = bk
        yk = y_k(bk, y0, k)
        y0 = yk
        k = k - 1
        return f(b0, y0, k)
    return f(b0, y0, k)
    
print(func(1, 3))
