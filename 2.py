try:
    a = int(input('Введите размерность 1 массива: '))
    b = int(input('Введите размерность 2 массива: '))
except ValueError:
    print('Это вещественное число, введите целое число')
    a = int(input('Введите размерность 1 массива: '))
    b = int(input('Введите размерность 2 массива: '))
arr_a = []
arr_b = []
for i in range(a):
    arr_a.append(float(input('Введите элемент 1 массива: ')))
for i in range(b):
    arr_b.append(float(input('Введите элемент 2 массива: ')))
arr_c = []
for i in range(a):
    for j in range(b):
        if arr_a[i] == arr_b[j]:
            arr_c.append(arr_a[i])
print('Элементы, которые содержатся в обоих массивах: ', *arr_c)
