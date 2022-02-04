"""
2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:

|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html

Примечание: структуру файла config.yaml придумайте сами,
его можно создать в любом текстовом редакторе «руками» (не программно);
предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""

import os
import yaml


def create_folders(list_of_folders, curdir):
    path_dir = None

    for folder in list_of_folders:
        if isinstance(folder, str):
            path_dir = os.path.join(curdir, folder)  # путь к создаваемой папке
            if not os.path.exists(path_dir):

                if os.path.splitext(folder)[1]:  # создание файлов с раширением
                    with open(path_dir, 'w', encoding='UTF-8'):
                        pass
                else:
                    os.makedirs(path_dir)  # создание папки

        else:  # если вложенная папка
            create_folders(folder, path_dir)


if __name__ == '__main__':
    # # Для создания yaml-config'а
    # folders_for_project = [
    #     'my_project', ['settings', ['some_file.py', '__init__.py', 'index.html'],
    #                    'mainapp',
    #                    'adminapp',
    #                    '.ssh',
    #                    'authapp'],
    # ]

    # with open('config.yaml', 'w') as f:
    #     yaml.dump(folders_for_project, f, default_flow_style=False)

    path = os.path.join(os.curdir)
    with open('config.yaml') as f:
        folders_for_project = yaml.safe_load(f)

    create_folders(folders_for_project, path)
