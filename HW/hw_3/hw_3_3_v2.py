# использовал set(spisok) - обошлись без подсчета кол-ва элементов count
# Сеты — НЕотсортированная коллекция Уникальных элементов, поэтому Сортировку надо перенести После сета!
def vvod_strok():
    sum_list = []
    while True:
        stri = input('Enter word: ')
        whitespace = ' \t\n\r\x0b\x0c'
        punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        excess_str = whitespace + punctuation
        new_str = stri
        for i in new_str:
            if i in excess_str:
                new_str = new_str.replace(i, ' ')
        stroka = new_str.lower()
        list = stroka.split(' ')
        if stri == '':
            break
        else:
            sum_list = list + sum_list
    return sum_list
full_list = vvod_strok()
#set(full_list) # убираем сетом повторяющиеся элементы списка. при этом формируется конструкция set([...])
list_unik = list(set(full_list))# конвентируем конструкцию из уникальных элементов опять в список. Все ок!
# print(list_unik) - все ок
list_unik.sort() # сортируем список по алфавиту,  но если создать переменную и присвоить ей значение этого отсортированного списка, то ОШИБКА при печати!!!
#print(list_unik) - все ок
for i in list_unik:
    print(i)
