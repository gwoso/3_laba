# 3_laba
## 7 вариант 
### Условие 1 задачи 
![image](https://github.com/gwoso/3_laba/assets/150545779/2f6d36da-8292-46d0-9ea4-1bd96551dec5)
### Алгоритм (рекурсия)
1. Создаём функцию `create_n_dim_array`, принимающую на вход значения `n`, `x`
2. Если `n <= 1`, то возвращаем `[f'level {n}']*x`
3. Иначе возвращаем функцию `[(create_n_dim_array(n-1, x))]`, умноженную на `x`
4. Выводим результат. Пусть `n = 2`, `x = 3`
### Результат
![image](https://github.com/gwoso/3_laba/assets/150545779/44ab3ca8-70c8-48c7-a95d-4e0cd94da5a6)
### Алгоритм (без рекурсии)
### Условие 2 задачи
![image](https://github.com/gwoso/3_laba/assets/150545779/fd6adbb2-9c20-424d-80c3-61718cc33d3b)
### Алгоритм (рекурсия)
1. Вводим создаём функцию `func`, которая примет на вход значения `x`, `k`
2. Проверяем `x` на положительность
3. Значения `b0 = 1 / (2 * x)` и `y0 = 1` даны по условию
4. Создаём функцию `f`, которая будет считать значаения `yk` и `bk`
5. Функция `b_k` считает значение `bk` через рекурсию
6. Функция `y_k` считает значение `yk` через рекурсию
7. Выводим результат функции при `x = 1` и `k = 3`
### Результат
![image](https://github.com/gwoso/3_laba/assets/150545779/c71cbcc1-6f97-4ab5-9692-53e7afde0453)
### Алгоритм (без рекурсии)
1. Вводим создаём функцию `func`, которая примет на вход значения `x`, `k`
2. Проверяем `x` на положительность
3. Значения `b0 = 1 / (2 * x)` и `y0 = 1` даны по условию
4. Создаём цикл, который будет действовать до тех пор, пока `k != 0`
5. Высчитвыаем значения `bk` и `yk`
6. Возвращаем и принтуем результат при `x = 1` и `k = 3`
### Результат 
![image](https://github.com/gwoso/3_laba/assets/150545779/079aa67c-832b-4f19-a4ca-283e40b9a6e0)
