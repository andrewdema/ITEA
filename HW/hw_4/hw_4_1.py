import string

def clear_word(word, filterstr):
    prav_simv = string.ascii_letters
    new_word = word
    for i in new_word:
        if i in filterstr:
            new_word = new_word.replace(i, '')
    for i in new_word:
        if i not in prav_simv:
            raise ValueError('The word has a outside symbol {}, index - {}'.format(i, word.index(i)))
    result = new_word
    return result


if __name__ == "__main__":
    slovo = 'fr$en%d'
    filter = 'afd'
    try:
        clear_word(slovo, filter)
    except ValueError as e:
        print(e)

    print(clear_word(slovo, filter))