"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:

|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

Примечание:
подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""

import os


def create_folders(list_of_folders, curdir):
    path_dir = None

    for folder in list_of_folders:
        if isinstance(folder, str):
            path_dir = os.path.join(curdir, folder)  # путь к создаваемой папке
            if not os.path.exists(path_dir):
                os.makedirs(path_dir)  # создание папки

        else:  # если вложенная папка
            create_folders(folder, path_dir)


if __name__ == '__main__':
    path = os.path.join(os.curdir)
    folders_for_project = [
        'my_project', ['settings',
                       'mainapp',
                       'adminapp',
                       'authapp'],
    ]

    create_folders(folders_for_project, path)
