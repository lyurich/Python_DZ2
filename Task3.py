# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8


number = int(input("Введите число: "))
square = 1
while square <= number:
    print(square, end=' ')
    square = square * 2
