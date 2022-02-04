"""
5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:

  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }

Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""

import os


def get_sizes(dir):
    """Получаем размеры файлов после рекурсивного обхода кратные 10ти"""
    files_count_dict = {}

    for dirpath, dirnames, filenames in os.walk(dir):
        for file in filenames:
            file = os.path.join(dirpath, file)
            size = os.path.getsize(file)
            ext = os.path.splitext(file)[1][1:]
            print(f'{ext:<15} {size:<15} {file:<15}')

            if size == 0:
                files_count_dict.setdefault(0, [0, set()])
                files_count_dict[0][0] += 1
                files_count_dict[0][1].add(ext)

            else:
                count = 1
                while True:
                    bite_level = 10 ** count

                    if not size // bite_level:
                        files_count_dict.setdefault(bite_level, [0, set()])
                        files_count_dict[bite_level][0] += 1
                        files_count_dict[bite_level][1].add(ext)
                        break
                    count += 1

    print('-' * 80)
    return files_count_dict


if __name__ == '__main__':
    dir = os.path.join(os.curdir)

    dict_files = get_sizes(dir)
    for k in sorted(dict_files.keys()):  # Печатаем результат
        print(k, ':', dict_files[k])
