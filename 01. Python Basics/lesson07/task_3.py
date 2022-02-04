"""
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, н

апример:

|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
это реальная задача, которая решена, например, во фреймворке django.
"""

import os
import shutil

root_dir = os.path.join(os.curdir, 'my_project')
templates_dir = os.path.join(os.curdir, 'my_project', 'templates')


def mk_dir_templates():
    for root, dirs, files in os.walk(root_dir):

        for file in files:
            ext = os.path.splitext(file)[1].lower()

            if ext == '.html':
                app_folder = os.path.basename(root)
                app_root = os.path.join(templates_dir, app_folder)
                html_root = os.path.join(root, file)
                html_dst = os.path.join(app_root, file)

                if not os.path.exists(app_root):
                    os.makedirs(app_root)

                if not os.path.exists(html_dst):
                    shutil.copy(html_root, html_dst)


if __name__ == '__main__':
    mk_dir_templates()
