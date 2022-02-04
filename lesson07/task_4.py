"""
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов
(в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0),

например:

    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...

Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""

import os
from collections import defaultdict


def get_sizes(dir):
    """Получаем размеры файлов после рекурсивного обхода кратные 10ти"""
    files_count_dict = defaultdict(int)

    for dirpath, dirnames, filenames in os.walk(dir):
        for file in filenames:
            file = os.path.join(dirpath, file)
            size = os.path.getsize(file)
            ext = os.path.splitext(file)[1][1:]
            print(f'{ext:<15} {size:<15} {file:<15}')

            if size == 0:
                files_count_dict[0] += 1

            else:
                count = 1
                while True:
                    bite_level = 10 ** count

                    if not size // bite_level:
                        files_count_dict[bite_level] += 1
                        break
                    count += 1

    print('-' * 80)
    return files_count_dict


if __name__ == '__main__':
    root_dir = os.path.join(os.curdir)

    dict_files = get_sizes(root_dir)
    for k in sorted(dict_files.keys()):  # Печатаем результат
        print(k, ':', dict_files[k])
