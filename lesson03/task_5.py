# ====================================== Задача 5 ======================================
"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]


Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""

import random


def get_jokes(iters: int = 7, *, repeat_mark=True) -> list[str]:
    """
    Фомрирует шутки в заданном колличестве
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    full = nouns, adverbs, adjectives
    max_len = max(map(lambda x: len(x), (nouns, adverbs, adjectives)))

    result = []
    # print(list(zip(nouns, adverbs, adjectives)))
    # Проверка на маркер повторения / повтор шутки iters-указанных раз
    if repeat_mark:
        for loop in range(iters):
            result.append(list(map(random.choice, full)))

    else:
        # Если не возможно использовать все элементы только 1 раз
        if iters > max_len: return ['введите меньшее колличество шуток', ]

        for loop in range(iters):
            # вынес лямбду для более удобной читаемости
            # seq.pop - удаление элемента из полследовательности и его возврат
            # seq.index - получение индекса рандомного элемента
            # random.choice(seq) - выбор рандомного элемента
            get_word = lambda seq: seq.pop(seq.index(random.choice(seq)))
            temp = map(get_word, full)
            result.append(tuple(temp))

    return list(map(lambda x: ' '.join(x), result))  # New

    # Old
    # for i, el_of_result in enumerate(result):
    #     result[i] = f'{el_of_result[0]} {el_of_result[1]} {el_of_result[2]}'
    # return result


if __name__ == '__main__':
    print(get_jokes(2))
    print(get_jokes(4, repeat_mark=False))
    print(get_jokes(10, repeat_mark=False))
