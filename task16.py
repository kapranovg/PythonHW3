# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

from random import randint

n = int(input("Введите максимальный элемент / длину массива: "))

array = [randint(0, n) for _ in range (n)]

print(array)

find_number = input("Введите искомую цифру: ")
count = 0
array_to_str = "".join(map(str, array))
new_array = list(array_to_str)

for i in new_array:
    if i == find_number:
        count += 1

print(f'Искомая цифра встречается {count} раз')
