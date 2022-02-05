```ad-quote
title:
## source:

## link:

```

#app/programs/git/local
#act/create
#os/linux

---

| Дерево         | Назначение                                      |
| :------------- | ----------------------------------------------- |
| Work directory | Песочница                                       |
| index          | Область для следующего коммита (предкоммит)     |
| HEAD           | Снимок последнего коммита (родитель следующего) |

```shell
# Просмотр всех дейсвий
git reflog


# Просмотр индекса и рабочей директории
git status 
```

## Work directory

песочница, где можно опробовать изменения перед их коммитом в индекс

```shell
# Добавление файлов в index
git add file
git stage file
```

## Index

то, что Git просматривает, когда вы выполняете `git commit`.

```shell
# файл добавлен в index
git rm --cached file # удалить из index
git rm -f file 		 # удалить из index из системы

# файл ИЗМЕНЕН после добавления в index
git restore --staged file # удалить из index (изменения сохранены)
git restore file 		  # оставить в index (изменения удалить)
```

## HEAD

Это значит, что HEAD будет родителем следующего созданного коммита. Как правило, самое простое считать HEAD снимком **вашего последнего коммита**.
запись текущего состояния в истории изменений!

```shell
# Создание коммита и перемещение в HEAD
git commit -m 'changes'  # запись коммита (перемещение в HEAD)
git commit -am 'changes' # добавление в index и запись коммита

# Изменение
git commit -am --amend   # изменить ранее записанный commit


# Просмотр коммитов
git log --oneline --graph --all #todo 
git diff <a9cb25e> <g8ewr2e>	# просмотр разницы между коммитами
git show						#todo 
```

# Other #todo

Заначка (Temporary storage)

```shell
```

## Pull-request #todo

## Tags #todo

```shell
git tag -a v1.4 -m 'my version 1.4'
git tag v1.4-lw
`-a, -s и -m`
```

## Слияние

## Перемещение
