def create_n_dim_array(n, x):
    if n <= 1:
        return [f'level {n}']*x
    return [(create_n_dim_array(n-1, x))] * x


print(create_n_dim_array(2, 3))
#n - n-мерность массива
#x - кол-во i, j, k... элементов
