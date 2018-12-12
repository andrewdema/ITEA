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
#print(full_list)


def voc(full_l):
    d = dict()
    for x in full_l:
        if x not in d:
            d[x] = 1
        else:
            d[x] = d[x] + 1
    return d
vocabulary = voc(full_list)
#print(vocabulary)

vocabulary.items() #это структура такого вида dict_items([(1, 'one'), (2, 'two'), (3, 'three')])
print('Статистика слов: ')
for key, value in vocabulary.items():
#print(key, '-', value)
    print('|{:<5}|{:^1}|'.format(key,value))








