# ====================================== Задача 3 ======================================
"""
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

Например:
thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"],
    "П": ["Петр"]
}

Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
Можно ли использовать словарь в этом случае?
"""


def thesaurus_1(names: list or tuple) -> dict:
    return_dict = {}

    for name in names:
        if name[0] not in return_dict:
            return_dict[name[0]] = [name, ]
        else:
            return_dict[name[0]].append(name)

    return return_dict


def thesaurus_2(names: list or tuple) -> dict:
    return_dict = {}
    names = sorted(names)  # сортировка по ключам (до внесения в словарь)

    for name in names:
        return_dict.setdefault(name[0], [])
        return_dict[name[0]].append(name)

    return return_dict


if __name__ == '__main__':
    name = "Иван", "Мария", "Петр", "Илья"
    assert thesaurus_2(name) == \
           thesaurus_1(name) == {"И": ["Иван", "Илья"],
                                 "М": ["Мария"],
                                 "П": ["Петр"]
                                 }
    print(thesaurus_2(name))
