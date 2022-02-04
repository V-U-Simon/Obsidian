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
    # Проверка на маркер повторения / повтор шутки iters-указанных раз
    if repeat_mark:
        # todo: сделать позднее через random.chosen
        for loop in range(iters):
            result.append(list(map(random.choice, full)))


    else:
        # todo: сделать позднее через random.sample
        # Если не возможно использовать все элементы только 1 раз

        # Для небольших последовательностей, через "тосовку"
        # list(map(random.shuffle, full))
        # return list(map(' '.join, zip(*full)))

        if iters > max_len: return ['введите меньшее колличество шуток', ]

        for loop in range(iters):
            # lambda:
            # random.choice(seq) - выбор рандомного элемента
            # seq.index - получение индекса рандомного элемента
            # seq.pop - удаление элемента из полследовательности и его возврат
            temp = map(
                lambda seq: seq.pop(seq.index(random.choice(seq))),
                full)
            result.append(tuple(temp))

    # New
    return list(map(lambda x: ' '.join(x), result))

    # Old
    # for i, el_of_result in enumerate(result):
    #     result[i] = f'{el_of_result[0]} {el_of_result[1]} {el_of_result[2]}'
    # return result


if __name__ == '__main__':
    print(get_jokes(2))
    print(get_jokes(4, repeat_mark=False))
    print(get_jokes(10, repeat_mark=False))
