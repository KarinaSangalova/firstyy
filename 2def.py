def getArray():
    try:
        n = int(input('Введите размерность массива: '))
    except ValueError:
        print('Это вещественное число. Введите целое число: ')
        n = int(input())
    array = []
    for i in range(n):
        array.append(float(input('Введите элемент массива: ')))
    return array


def ish_array():
    a = getArray()
    b = getArray()
    c = []
    for i in a:
        if i in b:
            c.append(i)
    return c

print('Элементы, которые содержатся в обоих массивах: ', *ish_array())