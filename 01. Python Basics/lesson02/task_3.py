# ====================================== Задача 3 ======================================
"""
*(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
Эта задача намного серьёзнее, чем может сначала показаться.
"""

source_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

index = 0
skip_marker = False  # маркер пропуска итерации: True - пропускаем, False - не пропускаем

for index, el in enumerate(source_list):
    # условие для исключения зацикливания
    if skip_marker:
        skip_marker = False
        continue

    if el.isalpha() or el == '"':
        pass
    elif el.isdigit():
        source_list[index] = f'{int(el):02}'  # форматируем цифры до двух знаков
        source_list.insert(index + 1, '"')  # правая кавычка
        source_list.insert(index, '"')  # левая кавычка
        skip_marker = True

    else:
        sign = el[0]
        digit = el[1:]
        source_list[index] = f'{int(el):02}'  # форматируем цифры до двух знаков
        source_list.insert(index + 1, '"')  # правая кавычка
        source_list.insert(index, '"')  # левая кавычка
        skip_marker = True

print(source_list)
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']


# приводим к строкам
for index, el in enumerate(source_list[1:]):
    if el.isalpha():
        source_list[0] += ' ' + el
    elif el.isdigit():
        source_list[0] += ' ' + el
    else:
        source_list[0] += ' ' + el

# удаляем пробелы
source_list = source_list[0]
index = 0
count_of_quotes = range(source_list.count('"'))
switch_by_quotes = True  # маркер открытия/закрытия кавычки: True - правая, False - левавя

for loop in count_of_quotes:
    index = source_list.index('"', index)

    if switch_by_quotes:
        # удаление правого пробела
        l_text = source_list[:index]
        r_text = source_list[index + 2:]
        switch_by_quotes = False
    else:
        # удаление левого пробела
        l_text = source_list[:index - 1]
        r_text = source_list[index + 1:]
        switch_by_quotes = True

    source_list = l_text + '"' + r_text
    index += 1  # перелкючиться на следующую кавычку

print(source_list)
