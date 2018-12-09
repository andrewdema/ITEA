# сделал, но есть вопрос в 21-й строке
# использовал set(spisok) - обошлись без подсчета кол-ва элементов count
# Сеты — НЕотсортированная коллекция Уникальных элементов, поэтому Сортировку надо перенести После сета!
def sort_word():
    def vvod_strok():
        sum_list = []
        while True:
            str = input('Enter word: ')
            str = str.lower()
            list = str.split(' ')
            if str == '':
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

sort_word()