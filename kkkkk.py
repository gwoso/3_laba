def create_n_dim_array(n, x):
    if n == 2:
        print("[")
        for a in n:
            print([f'level {n}'] * x)
        print("]")
    if n == 3:
        print("[")
        for a in n:
            print("[")
            for b in a:
                print([f'level {n}'] * x)
            print("]")
        print("]")
    biba = [f'level {n}'] * x
    for i in range(n-1):
        biba = [biba.copy() for j in range(x)]
    return biba

print(create_n_dim_array(2, 3))
