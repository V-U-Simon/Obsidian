# ====================================== Задача 2 ======================================
"""
Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками 
(добавить кавычку до и кавычку после элемента списка, являющегося числом) 
и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? 
Как модифицировать это условие для чисел со знаком?

Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. 
Главное: дополнить числа до двух разрядов нулём!
"""

source_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
target_list = []

for el in source_list:
    if el.isalpha():
        target_list.extend([el])
    elif el.isdigit():
        target_list.extend(['"', f'{int(el):02}', '"'])
    # elif (el[0] == '+' or el[0] == '-') and el[1:].isdigit(): # условие для чисел со знаком
    # Но уж очень понравился лайвхак из прошлого занятия, связанный с потоком выполениния и ветвлением)) P.S. спасибо :)
    else:
        sign = el[0]
        digit = el[1:]
        target_list.extend(['"', sign + f'{int(digit):02}', '"'])

print(target_list)

# удаление пробелов около - "
result_list = ' '.join(target_list)

index = 0
count_of_quotes = range(result_list.count('"'))
switch_by_quotes = True  # маркер открытия/закрытия кавычки: True - правая, False - левавя

for loop in count_of_quotes:
    index = result_list.index('"', index)

    if switch_by_quotes:
        # удаление правого пробела
        l_text = result_list[:index]
        r_text = result_list[index + 2:]
        switch_by_quotes = False
    else:
        # удаление левого пробела
        l_text = result_list[:index - 1]
        r_text = result_list[index + 1:]
        switch_by_quotes = True

    result_list = l_text + '"' + r_text
    index += 1  # перелкючиться на следующую кавычку

print(result_list)