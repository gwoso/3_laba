def create_n_dim_array(n, x):
    biba = [f'level {n}'] * x
    for i in range(n-1):
        biba = [biba.copy() for _ in range(x)]
    return biba

def printf(n, result):
    if n == 2:
        print("[")
        for a in result:
            print("\t", a)
        print("]")

    if n == 3:
        print("[")
        for a in result:
            print("\t [")
            for b in a:
                print("\t\t", b)
            print("\t ]")
        print("]")

n = int(input("Enter n: "))
x = int(input("Enter x: "))

result = create_n_dim_array(n, x)
printf(n, result)
