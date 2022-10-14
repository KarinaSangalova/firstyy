try:
    n = int(input('Введите размерность массива: '))
except ValueError:
    print('Это вещественное число. Введите целое число: ')
    n = int(input())
arr = []
for i in range(n):
    arr.append(float(input('Введите элемент массива: ')))
kmax = 0
imax = 0
for i in range(n):
    if arr[i] >= kmax:
        kmax = arr[i]
        imax = i
for i in range(n):
    if i > imax:
        arr[i] = 0
print('Исходный массив: ', arr)