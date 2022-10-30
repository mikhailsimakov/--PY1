def get_count_char(str_):
    str_1 = ''.join(str_.lower().split())
    str_2 = ''
    dictionary = {}
    DEFAULT_COUNT = 0
    for i in range(len(str_1)):
        if str_1[i].isalpha():
            str_2 += str_1[i]
    for symbol in str_2:
        dictionary[symbol] = dictionary.get(symbol, DEFAULT_COUNT) + 1
    return dictionary


def get_percent_char(dictionary_):
    dictionary_percent = {}
    dictionary_sum = sum(dictionary_.values())
    for key, value in dictionary_.items():
        dictionary_percent[key] = round(((dictionary_[key]) / dictionary_sum) * 100, 3)
    return dictionary_percent


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
# функцию, которая принимает строку и возвращает словарь с частотой каждого символа
print(get_count_char(main_str))
# словарь символов
dictionary_2 = get_count_char(main_str)
# функция где количество каждого элемента заменено на процентное отношение ко всем символам
print(get_percent_char(dictionary_2))
