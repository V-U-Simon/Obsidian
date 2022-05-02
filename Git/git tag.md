---
aliases: ['git tags', ]
created: 2022.04.26 9:31:42 am
modified: 2022.04.29 11:21:28 am
---

#application🛠/Git⏳
#application🛠/Git⏳/commit
#🏃/show

>[!cite]- Source
>- ⭐ [bitbucket - Git tag](https://www.atlassian.com/ru/git/tutorials/inspecting-a-repository/git-tag)
>- ⭐ [Основы Git - Работа с тегами](https://git-scm.com/book/ru/v2/Основы-Git-Работа-с-тегами)

Виды тегов:

> отличаются объемом метаданных

- аннотируемые
- облегченные


```Bash
# Список
git tag 
git tag -l tag_v* # поиск по глоб шаблону
# tag_v1.2
# tag_v1.1


# Создание
git tag <tagname>        # cоздание облегченного тега   
git tag <tagname> <HEAD> # тег для другого коммита
-a # cоздание аннотируемого тега
-s 
-m # добавление сообщения (аннотируемый тег)


# Перезапись тега
git tag -f v1.4 15de7 # force - принудительная перезапись тега


# Удаление 
git tag -d v1.4


# Действия с тегом
git checkout v1.4
git push origin v1.4
```
