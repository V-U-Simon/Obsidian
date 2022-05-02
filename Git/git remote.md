---
aliases: ['yдаленный репозиторий','remote repository', ]
created: 2022.02.13 10:01:53 pm
modified: 2022.04.29 9:29:07 pm
---

#application🛠/Git⏳/Repository

>[!cite]- Source
> - <https://ru.stackoverflow.com/questions/431520/Как-вернуться-откатиться-к-более-раннему-коммиту>
> - ⭐ [Работа с удалёнными репозиториями](https://git-scm.com/book/ru/v2/Основы-Git-Работа-с-удалёнными-репозиториями)
> - <https://open2web.com.ua/blog/kak-vernutsya-otkatitsya-k-bolee-rannemu-kommitu.html>

>[!example]- Index
> - [[git remote]]
> - [[git branch]]
> - [[git fetch | fetch]] (принести) получение данных
> - [[git pull]] (тянуть) приминение изменений
> - [[git push]] (толкать) отправка изменений

**`git remote`** - служит для управления списком удалённых репозиториев.
позволяет сохранять длинные URL репозиториев в виде понятных коротких строк, например "origin"

# настройка удаленных репозиториев

```shell
# ПРОСМОТР удаленного репозитория
git remote                       # удаленные подключения к другим репозиториям
git remote -v                    # список репо + адреса(ссылки - url)
git remote show <remote_repo>    # заглянуть в удаленный репозиторий
# прочee
git remote get-url <remote_repo> # url ссылка репозитория
git ls-remote <remote_repo>	     # ссылки на коммиты удаленных веток (sha)


# СОЗДАНИЯ записи о новом подключении к удаленному репозиторию
git remote add <remote_name> <remote_repo_url> # Добавляет в `./.git/config`
# git remote add new_repo www@85.123.172.123:/home/www/code/project_dir
# git fetch remote_repo rm_br # скачивание удаленной ветки на локульную машину
# В последствии можно воспринимать как локальную ветку
# но с возможностью вытягивать обновления с сервера


# ПЕРЕИМЕНОВАНИЕ удаленного подключения
git remote rename old_name new_name   # Обновляет ./.git/config
# УДАЛЕНИЕ подключения к удаленному репозиторию
git remote remove name_of_repo        # long - remove
git remote rm name_of_repo			  # short - rm


# ОТПРАВКА данных в удаленные репозитории 
git push remote_repo local_br # состояние локальной ветки передается в удаленный репозиторий
```
