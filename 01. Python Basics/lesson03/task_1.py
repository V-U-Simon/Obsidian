# ====================================== Задача 1 ======================================
"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.

Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"

Если перевод сделать невозможно, вернуть None.
Подумайте, как и где лучше хранить информацию, необходимую для перевода:
какой тип данных выбрать, в теле функции или снаружи.
"""


def num_translate(word: str) -> str:
    dictionary = {
        "one": 'один',
        "two": 'два',
        "three": 'три',
        "four": 'четыре',
        "five": 'пять',
        "six": 'шесть',
        "seven": 'семь',
        "eight": 'восемь',
        "nine": 'девять',
        "ten": 'десять',
    }

    return dictionary.get(word, 'write number from 1 to 10')
    # return dictionary[word]

if __name__ == '__main__':
    assert num_translate('one') == 'один'
    assert num_translate('ten') == 'десять'
    assert num_translate('eleven') == 'write number from 1 to 10'
    assert num_translate('') == 'write number from 1 to 10'

    # assert num_translate(1) == 'write number from 1 to 10'
    # assert num_translate(0.5) == 'write number from 1 to 10'
    # assert num_translate(True) == 'write number from 1 to 10'
    # assert num_translate(None) == 'write number from 1 to 10'
    print('The test was successful')