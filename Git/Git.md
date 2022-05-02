---
aliases: [ ]
created: 2022.02.13 10:01:53 pm
modified: 2022.04.29 4:54:51 pm
---

#application🛠/Git⏳
#OS🖥/Linux

>[!cite]- Source
> - ℹ️  [Документация](https://git-scm.com/book/ru/v2/Git-на-сервере-Настраиваем-сервер)
> - [Git снизу вверх](https://habr.com/ru/company/intel/blog/344962/)
> - [Ежедневная работа с Git](https://habr.com/ru/post/174467/)
> - [Git и публикация сайта](https://habr.com/ru/post/127213/)
> - [использование собственного Git-сервера](https://habr.com/ru/company/ruvds/blog/359216/)
> - [Git для новичков (часть 1)](https://habr.com/ru/post/541258/)
> ---
> - <https://losst.ru/kompilyatsiya-programm-linux>
> - [Подготовка системы](https://losst.ru/kompilyatsiya-programm-linux#%D0%9F%D0%BE%D0%B4%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D0%BA%D0%B0_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B)
> - [Как выполняется компиляция?](https://losst.ru/kompilyatsiya-programm-linux#%D0%9A%D0%B0%D0%BA_%D0%B2%D1%8B%D0%BF%D0%BE%D0%BB%D0%BD%D1%8F%D0%B5%D1%82%D1%81%D1%8F_%D0%BA%D0%BE%D0%BC%D0%BF%D0%B8%D0%BB%D1%8F%D1%86%D0%B8%D1%8F)
> - [Компиляция программ Linux](https://losst.ru/kompilyatsiya-programm-linux#%D0%9A%D0%BE%D0%BC%D0%BF%D0%B8%D0%BB%D1%8F%D1%86%D0%B8%D1%8F_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC_Linux)
> - [Получение исходников](https://losst.ru/kompilyatsiya-programm-linux#%D0%9F%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B8%D1%81%D1%85%D0%BE%D0%B4%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2)
> - [Настройка configure](https://losst.ru/kompilyatsiya-programm-linux#%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0_configure)
> - [Сборка программы](https://losst.ru/kompilyatsiya-programm-linux#%D0%A1%D0%B1%D0%BE%D1%80%D0%BA%D0%B0_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B)
> - [Выводы](https://losst.ru/kompilyatsiya-programm-linux#%D0%92%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)
> ---
> - ⭐[git config](https://www.atlassian.com/ru/git/tutorials/setting-up-a-repository/git-config)
> - ⭐ [git alias](https://www.atlassian.com/ru/git/tutorials/git-alias)
> - [Шпоргалка](https://proglib.io/p/git-cheatsheet)


>[!example]- Index
>
>- [[Просмотр репозитория]]
> 	- [[git status]]
> 	- [[git diff]]
> 	- [[git log]]
> 	- [[git reflog]]
> 	- [[git tags]]
>- [[Совместная работа]]
>- [[Сохранение изменений]]
>	- [[Commit]]
>	- [[Отмена изменений]]
>	- [[Переписывание истории]]
> - [[- область видимости файлов | Область видимости файлов в репозитории]]
> - [[git restore]]
> - [[git stash (спрятать файл)]]
>- Создание репозитория
> 	- [[git init]]
> 	- [[git clone]]
> 	- [[git remote#^894068 | git remote add]]
> - Commit
> 	- [[git reset]]
> 	- [[git revert]]
> 	- [[git restore]]
> 	- [[git merge]]
> 	- [[git rebase]]
> - [[git push]]
>- [[Совместная работа]]
>- [[gitignore]]


**Git** - система контроля версий

Управление git сервером включает в себя:
- умение добавлять новые репозитории
- умение удалять устаревшие репозитории,
- умение управлять различными удалёнными ветками
- объявлять их отслеживаемыми или нет

# Install

```shell
apt-get install git # linux
brew install git    # MacOS
```

# Config

Git хранит варианты конфигурации в трех различных файлах, позволяющих ограничивать область видимости на уровне отдельных репозиториев (локальный), пользователя (глобальный) или всей системы (системный):

```Bash
/.git/config # Локальный — на уровне репозитория.
/.gitconfig  # Глобальный — на уровне пользователя. Здесь хранятся настройки с флагом --global.
$(prefix)/etc/gitconfig # Системный — на уровне всей системы.
```

```Bash
git config --global user.name <name>
git config --local user.email <email>


# Опциональная установка алиасов
git config --global alias.<alias-name> <git-command>
# примеры
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'reset HEAD --'
# git unstage fileA == git reset HEAD -- fileA
git config --global alias.last 'log -1 HEAD'
git last
#  commit 66938dae3329c7aebe598c2246a8e6af90d04646
#  Author: Josh Goebel <dreamer3@example.com>
#  Date:   Tue Aug 26 19:48:51 2008 +0800
#
#  test for current head
#       Signed-off-by: Scott Chacon
# <schacon@example.com>
```

# Setting

```shell
config      # содержит специфичные для этого репозитория конфигурационные параметры
description # используется только программой GitWeb
hooks/      # располагаются клиентские и серверные хуки
info/       # расположен файл с глобальными настройкам игнорирования файлов

HEAD        # указывает на текущую ветку
index		# хранится содержимое индекса
objects/    # база данных объектов Git
refs/       # ссылки на объекты коммитов в этой базе (ветки, теги и другие)
```

