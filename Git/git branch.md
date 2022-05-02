---
aliases: ['локальная ветка', ]
created: 2022.04.22 9:43:02 pm
modified: 2022.04.30 9:23:04 am
---
#application🛠/Git⏳/branch

>[!cite]- Source
> - ⭐ [Синхронизация в Git](https://www.atlassian.com/ru/git/tutorials/syncing)

**`git branch`** - позволяет создавать, просматривать, переименовывать и удалять ветки.

❌ не дает возможности переключаться между ветками или выполнять слияние разветвленной истории

# локальные ветки

```Bash
git branch -vv -a # список веток с указателями + отслеживание удаленных 
git branch        # Просмотр локальных веток
git branch -a     # Просмотр всех известных веток
git branch -r     # Просмотр указателей удаленных веток
git branch -v     # Просмотр указателей веток


# Создение / Удаление / Переименование
git branch      br_name      # создание ветки
git checkout -b br_name      # создание от HEAD и переключение | git checkout -b br_name HEAD
git checkout -b br_name HEAD # создение ветки в месте указателя
git branch -m   br_name      # переименование
git branch -c   br_name      # копирование ветки
git branch -d   br_name      # удаление (безопастное)
git branch -D   br_name      # удаление (даже не слитых изменений)

# создание ветки в папке
git branch folder_1/folder_2/br_name       

# Переключение
git checkout branch    # переключится на другую ветку
```

## отслеживание удаленных веток

```Bash
# git remote add rm_repo <url>    # добавили url удаленного репозитория
# git fetch rm_repo rm_br         # скачали удаленную ветку на локальную машину


# Создать локальную ветку на основе удаленной ветки (+отслеживать)
git branch      local_br rm_repo/rm_br # создание локальной ветки на месте удаленной
git checkout -b local_br rm_repo/rm_br # создание локальной ветки на месте удаленной
# Создать удаленную ветку на основе локальной 
git push -u rm_repo HEAD:rm_br # отрпавить данные из HEAD на rm_br (если нет, создать + отслеживать)
git push    rm_repo HEAD:rm_br # отрпавить данные из HEAD на rm_br (если нет, создать)


# ОТСЛЕЖИВАТЬ на текущей ветке
git branch -u rm_repo/rm_br                # short 
git branch --track rm_repo/rm_br           # middle
git branch --set-upstream-to rm_repo/rm_br # long
# ПЕРЕСТАТЬ ОТСЛЕЖИВАТЬ на текущей ветке
git branch --unset-upstream 
```

# удаленные ветки на сервере

```shell
# git remote add rm_repo <url>
# git fetch rm_repo rm_br 


# Создать ветку на сервере
git push -u rm_repo local_br         # поместит локальную ветку в удаленный репозиторий
git push    rm_repo local_br:newname # переименование ветки на сервере


# удаление ветки на сервере
git branch -d -r rm_repo/rm_br
git push         rm_repo --delete rm_br
git push         rm_repo  :rm_br # short way | git push rm_repo --delete rm_br


# Переименовать удаленную ветку на сервере
# !!! последовательность действий
git branch -m br_old_name br_new_name
git fetch origin
git branch -u origin/br_new_name br_new_name
git remote set-head origin -a


# Отправить изменения на сервер
git push rm_repo rm_repo/rm_br
```

# удаление ветки локально и на сервере

```Bash
git branch -D branch_name    # сотрет локальную ветку с именем branch_name
git push origin :branch_name # сотрет удаленную ветку с именем branch_name
```
