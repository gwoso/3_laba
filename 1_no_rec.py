def create_n_dim_array(n, x):
    biba = [f'level {n}'] * x
    for i in range(n-1):
        biba = [biba.copy() for _ in range(x)]
    return biba

result = create_n_dim_array(2, 3)
for row in result:
    print(row)
