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
full_list.sort()
for i in full_list:
    print(i)


