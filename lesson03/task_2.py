# ====================================== Задача 2 ======================================
"""
*(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
Например:
num_translate_adv("One")
"Один"
num_translate_adv("two")
"два"
"""


def num_translate_adv(word: str) -> str:
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

    if word.istitle():
        return dictionary.get(word.lower(), 'Error').title()
    else:
        return dictionary.get(word, 'Error')


if __name__ == '__main__':
    assert num_translate_adv('one') == 'один'
    assert num_translate_adv('One') == 'Один'
    assert num_translate_adv('ten') == 'десять'
    assert num_translate_adv('Ten') == 'Десять'

    assert num_translate_adv('') == 'Error'
    assert num_translate_adv('Eleven') == 'Error'
    assert num_translate_adv('eleven') == 'Error'
    print('The test was successful')
