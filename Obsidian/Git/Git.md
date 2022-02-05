```ad-quote
title:
## source:
- [Документация](https://git-scm.com/book/ru/v2/Git-на-сервере-Настраиваем-сервер)
- [Git снизу вверх](https://habr.com/ru/company/intel/blog/344962/)
- [Ежедневная работа с Git](https://habr.com/ru/post/174467/)
- [Git для новичков (часть 1)](https://habr.com/ru/post/541258/)
- [Git и публикация сайта](https://habr.com/ru/post/127213/)
- [использование собственного Git-сервера](https://habr.com/ru/company/ruvds/blog/359216/)
## link:
- 
```

#app/programs/git/local
#os/linux

---

Git - контентно-адресуемая файловая система.

```shell
$ ls -F1
config      # содержит специфичные для этого репозитория конфигурационные параметры
description # используется только программой GitWeb
hooks/      # располагаются клиентские и серверные хуки
info/       # расположен файл с глобальными настройкам игнорирования файлов

HEAD        # указывает на текущую ветку
index		# хранится содержимое индекса
objects/    # база данных объектов Git
refs/       # ссылки на объекты коммитов в этой базе (ветки, теги и другие)
```

## Область видимости файлов

```shell
.gitignore 	# игнорируемые файлы
.gitkeep 	# в случае неоходимости добавления пустых папок
```

- [генератор файлов .gitignore](https://www.toptal.com/developers/gitignore)