print('Введите массив (значения вводите через пробел) : ')
array = [float(dx) for dx in input().split()]
delta = float(input('Введите значение delta: '))
min_array = 10**10
for i in range(len(array)):
    if min_array > array[i]:
        min_array = array[i]
k = 0
for i in range(len(array)):
    if array[i] - min_array == delta:
        k += 1
print('Количество элементов в заданном массиве, отличающихся от минимального на delta: ', k)

