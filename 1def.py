try:
    n = int(input('Введите размерность массива: '))
except ValueError:
    print('Это вещественное число. Введите целое число: ')
    n = int(input())
def getArray():
    array = []
    for i in range(n):
        array.append(float(input('Введите элемент массива: ')))
    return array

def ish_array():
    array = getArray()
    max_elem = 0
    imax = 0
    for i in range(len(array)):
        if max_elem < array[i]:
            max_elem = array[i]
            imax = i
    for i in range(len(array)):
        if i > imax:
            array[i] = 0
    return array

print(ish_array())