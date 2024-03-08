def create_n_dim_array(n, x, level = 1):
    if n <= 1:
        return [f'level {level}']*x
    return [(create_n_dim_array(n-1, x, level + 1))] * x


result = create_n_dim_array(2, 3)
for row in result:
    print(row)
