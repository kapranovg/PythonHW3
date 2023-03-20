# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint

numbers_length = int(input("Введите длину / максимальный элемент массива: "))
numbers = [randint(0, numbers_length) for _ in range(numbers_length)]
print(numbers)

sorted_numbers = [i for i in set(numbers)]
print(sorted_numbers)

x = int(input("Введите искомое число: "))
closest_number = sorted_numbers[0]
for i in sorted_numbers:
    if abs(x - i) <= abs(closest_number - i):
        closest_number = i

print(f'Наиболее близкое число к {x} в текущем массиве - число {closest_number}')
