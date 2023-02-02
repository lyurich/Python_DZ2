# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# *Пример:
# 5 -> 1 0 1 1 0
# 2

from random import randint
number_coins = int(input('Введите количество монет: '))
reshka = 0
# orel = 1
for i in range(number_coins):
    coins = randint(0, 1)
    print(coins, end=' ')
    if coins == 1:
        reshka += 1
print(f'\nНужно перевернуть {reshka if reshka<number_coins/2 else number_coins - reshka} монет')







