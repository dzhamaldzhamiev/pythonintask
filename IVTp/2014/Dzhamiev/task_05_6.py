# Задача 5. Вариант 6.
# Напишите программу, которая бы при запуске случайным образом отображала название одного из двух спутников Марса.

# Dzhamiev D. R.
# 11.04.2016


from random import choice

phrase = 'Фобос, Деймос'

nephews = [''.join(filter(str.isalpha, name))
           for name in phrase.split(' ')
           if len(name) > 2]

stats = dict((nephew, 0) for nephew in nephews)

print("Случайный племянник Скруджа МакДака.")

k = 1
while True:
    c = choice(nephews)
    stats[c] += 1
    k -= 1
    if k <= 0:
        print('\n' + c)
        print('Статистика ' + str(stats))
        try:
            k = int(input('Повторить n раз (0 чтобы выйти): '))
            if k <= 0:
                break
        except:
            continue
