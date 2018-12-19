from string import whitespace, punctuation, digits, ascii_letters, ascii_lowercase, ascii_uppercase

def get_eng_words(text):
    #symbol not in string.ascii_letters + string.digits + string.punctuation + string.whitespace
    text = text.lower()
    my_list = text.split(' ')
    my_list_unic = set(list(my_list))
    for i in my_list_unic: # для всех элементов (строк) из уникального списка мы запускаем функцию по замене в этих строках ненужных символов на пустоту
        from hw_4_1 import clear_word # i  - это word, а filterstr(filter) определим как сумма строк из ненужных символов
    result = my_list_unic
    return result

if __name__ == "__main__":
    TEXT = "What is world? В Data Science язык программирова\tния Python нашёл широкое применение. НепRавильные сл0ва сЦ1фрам - 123"
    filter = whitespace + punctuation + digits
    print(get_eng_words(TEXT))