from string import whitespace, punctuation

def get_vocabluary(text):
    excess_str = whitespace + punctuation
    new_str = text
    for i in new_str:
        if i in excess_str:
            new_str = new_str.replace(i, ' ')
    stroka = new_str.lower()
    spisok = stroka.split(' ') # текст(строки) превращаем в список
    #set(spisok) # убираем сетом повторяющиеся элементы списка. при этом формируется конструкция set([...])
    list_unik = list(set(spisok))  # конвентируем конструкцию из уникальных элементов опять в список. Все ок!
    list_unik.sort()  # сортируем список по алфавиту,  но если создать переменную и присвоить ей значение этого отсортированного списка, то ОШИБКА
    result = list_unik

    return result

# if __name__ == "__main__":
#     print("Running the main program code")

TEXT = """Здесь определяется  работы + -./ : программы. и, я знаки ,например ; <=>?@"""

my_list = get_vocabluary(TEXT) # используем гобальную переменную ТЕХТ (это не желательно делать)
# print(my_list)


# функция на удаление 'ненжуных' символов (чистим строку, но от цифр не очищает!):
def clearing(clean_str):
    excess_str = whitespace + punctuation
    for i in excess_str:
            clean_str = clean_str.replace(i, '')
    return clean_str

# Ниже блок кода по релизации вывода на экран полученного словаря слов:
def vocabulary(my_copy_list):
    dict_full = {} # создадим пустой словарь, который будем далее заполнять словами из текста (ключами) и введенными переводами (значениями)
    for x in my_copy_list:
        loop = False # флаг для цикла
        while loop == False:
            enter = input('Please enter translation for word {}: '.format(x))
            if clearing(enter).isalpha() == True:
                loop = True  # останавливаем цикл, если слово чистое
                add_para = {x:clearing(enter)}
                dict_full.update(add_para)
            else:
                print('Input Error. Please enter the word again!')
    return dict_full

s = vocabulary(my_list)

s.items() #это структура такого вида dict_items([(1, 'one'), (2, 'two'), (3, 'three')])
print('Словарь:')
for key, value in s.items():
    #len(key)
    #print(key, '-', value)
    print('{:<20}<{:^4}>'.format(key,value))


