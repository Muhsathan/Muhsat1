p = input('Напишите сообщение боту: ')
while p != 'Пока':
    dict1 = {
        'q': 'Программа',
        'w': 'Работаю',
        'e': 'Хорошо',
        'r': 'Как-то',
        't': 'У тебя на компе',
    }
    if p == 'Кто ты?':
        print(dict1['q'])
    elif p == 'Что ты делаешь?':
        print(dict1['w'])
    elif p == 'Как дела?':
        print(dict1['e'])
    elif p == 'Как это работает?':
        print(dict1['r'])
    elif p == 'Где ты?':
        print(dict1['t'])
    p = input('Напишите сообщение боту: ')
dictionary_1 = {
    'a': 300,
    'b': 400,
}
dictionary_2 = {
    'c': 500,
    'd': 600,
}
dictionary_1 |= dictionary_2
print(dictionary_1)




