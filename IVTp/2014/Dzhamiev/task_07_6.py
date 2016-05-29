# Задача 6. Вариант 6.
# Создайте игру, в которой компьютер загадывает название одного из семи городов России, имеющих действующий метрополитен, а игрок должен его угадать.

# Dzhamiev D. R.
# 11.04.2016


from random import choice

print('Угадайте один из семи городов России, имеющий действующий метрополитен!')

cities = tuple('Москва Петербург Новгород Новосибирск Самара Екатеринбург Казань' .split())

cities = [x.lower() for x in cities]

right = choice(cities)
trys = []

score_unit = 10
score = score_unit * len(cities)


k = 1
while True:
    print('\n', k, 'попытка.. У вас', score, 'очков.')
    word = input('> ').lower()
    
    if right == word:
        print('Правильно! Это', right + '!')
        print('Вы заработали', score, 'очков!')
        input('\nНамите Enter...')
        break
    
    if word not in cities:
        print('Такого города нет')
        continue
    
    if word in trys:
        print('Вы уже пробовали', word)
        continue
    trys.append(word)
    score -= score_unit
    
    k += 1
    if k == 4:
        print('Подсказка: последниие две буквы -', right[-2:])
        
    elif k == 6:
        r = cities.index(right)
        print('Подсказка:', cities[r-1], '...',
              cities[r+1 if r < len(cities)-1 else 0])
