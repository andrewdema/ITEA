#сделал
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
    full_list.sort()
    for i in full_list:
        n = full_list.count(i)
        while n != 1:
            full_list.remove(i)
            n = full_list.count(i)
        print(i)

sort_word()