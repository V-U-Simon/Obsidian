---
aliases: [ ]
created: 2022.04.24 6:07:47 pm
modified: 2022.04.27 11:33:20 am
banner: "https://wac-cdn.atlassian.com/dam/jcr:52d530ce-7f51-48e3-920b-a18f776048d3/01.svg?cdnVersion=313"
banner_x: 0.5
---

#application🛠/Git⏳
#🏃/show

>[!cite]- Source
>
>- ⭐ [git diff](https://www.atlassian.com/ru/git/tutorials/saving-changes/git-diff)

# просмотр истории коммитов

**`git diff`** -  сравнение источников данных Git — коммитов, веток, файлов и т. д.

```shell
#						   WD
git diff                 # WD - index 
git diff HEAD            # WD --------- HEAD
git diff HEAD~           # WD ---------------- HEAD~
#						  		index
git diff                 # WD - index 
git diff --cached        #      index - HEAD
git diff --cached  HEAD~ #      index -------- HEAD~
#						  		        HEAD
git diff --cached        #      index - HEAD
git diff HEAD            # WD --------- HEAD
git diff HEAD HEAD~      #              HEAD - HEAD~
```

# дополнительные аргументы

```shell
git diff -- file       # `--`  для просмотра опредленнного файла
git diff-highlight     # Сопоставление строк 
git diff --color-words # с цветовой подсветкой
```
