def create_n_dim_array(n, x):
    biba = [f'level {n}'] * x
    for i in range(n-1):
        biba = [biba.copy() for j in range(x)]
    return biba

print(create_n_dim_array(2, 3))
#n - n-мерность массива
#x - кол-во i, j, k... элементов
