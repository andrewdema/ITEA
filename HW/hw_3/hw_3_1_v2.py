'''Рассуждения - вводим строки пока не ввели пустую (while). Сразу строку превращаем в список (split) и складываем все
строки(списки) в один список. Возращаем из ф-ии общий список и вводим переменную, которой присваиваем этот общий список.
Далее этот список превращаем в словарь. В словаре ключ - это слова, которые мы вводили в строках, а значение - количество
повторений этих слов. Отдельной функцией считаем количество повторений в списке и возвращаем результат.
ВОПРОС в словаре(список(ключи), результат(значения)) - не понятно что вписать в значение??? (еще не проходили), поэтому
я написал пока вторым способом - воспользовался модулем Counter, который формирует сразу словарь, но в кортеже со
статистикой слов.
Чтобы вывести на печать ключ: значение, надо из словарь сделать структуру items - for key, value'''

def vvod_strok():
    sum_list = []
    while True:
        str = input('Enter word: ')
        stroka = str.lower()
        list = stroka.split(' ')
        if str == '':
            break
        else:
            sum_list = list + sum_list
    return sum_list

full_list = vvod_strok()
##print(full_list)

# def povtorenie():
#     for i in full_list:
#         kol_povt = full_list.count('i')
#         return kol_povt
# povtor_slov = povtorenie()

##print(povtor_slov)
# так как в словаре не может быть двух одинаковых ключей, то все слова будут в единичном экземпляре или использовать while, как в 3й задаче?


# первый способ (с ОШИБКОЙ - не знаю как сформировать значение в словаре - пробовал вместо значения вызывать ф-ию и писать
# то, что возвращает ф-ия, но не работает!
#dictionary = dict.fromkeys(full_list, povtorenie()) #создаем из списка словарь: full_list - данный список (его элементы будут ключами,
# а после запятой указываем значение - повторения слов)
##print(dictionary)
#struktura = dictionary.items()
# print('Статистика слов: ')
# for key, value in dictionary.items():
#     print(key, '-', value)

# второй способ более простой, так как срау считается кол-во повторений для каждого слова в списке:
from collections import Counter
result = Counter(full_list) # формирует словарь в кортеже со статистикой слов, в котором слова являются ключами, а значения - количество повторений слова
dictionary = dict(result) # результат (конструкция в виде словарь в кортеже) превращаем в словарь
# чтобы вывести на печать ключи и значения, методом items превращаем словарь в конструкцию состоящую из ключ/значение в кортежах,
# которые через запятую образуют список размещенный в кортеже: вид dict_items([(1, 'one'), (2, 'two'), (3, 'three')])
#struktura = dictionary.items()
print('Статистика слов: ')
for key, value in dictionary.items():
    #print(key, '-', value)
    print('|{:<5}|{:^1}|'.format(key,value))