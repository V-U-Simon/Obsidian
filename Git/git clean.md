---
aliases: [ ]
created: 2022.04.27 4:35:24 pm
modified: 2022.04.27 4:42:26 pm
---
#application🛠/Git⏳

>[!cite]- Source
>- ⭐ [Git clean](https://www.atlassian.com/ru/git/tutorials/undoing-changes/git-clean)

** `git clean`** -  команда удаления неотслеживаемых файлов в рабочем каталоге репозитория.

> **Неотслеживаемые файлы** - это файлы в каталоге репозитория, которые еще не добавлены в раздел проиндексированных файлов репозитория

- По умолчанию `git clean` не обрабатывает каталоги рекурсивно

```Bash
git clean 
git clean -n

-d # directory 
-x # обрабатывает все игнорируемые файлы
-i # интерактивный режим
```
