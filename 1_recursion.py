def create_n_dim_array(n, x, level = 1):
    if n <= 1:
        return [f'level {level}']*x
    return [(create_n_dim_array(n-1, x, level + 1))] * x

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
