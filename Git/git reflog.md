---
aliases: [ ]
created: 2022.04.27 12:10:39 pm
modified: 2022.04.27 3:38:21 pm
---
#application🛠/Git⏳
#🏃/show

>[!cite]- Source
>- ⭐ [git reflog](https://www.atlassian.com/ru/git/tutorials/rewriting-history/git-reflog)

**`git reflog`** - отслеживает изменения в конце веток с помощью механизма журналов ссылок.


журналов ссылок для последних коммитов ветки
журнал ссылок команды git stash

Журналы ссылок хранятся в подкаталогах внутри каталога .git локального репозитория.

```Bash
# Места хранения журналов
git reflog # .git/logs/refs/heads/. и .git/logs/HEAD, а также 
git stash  # .git/logs/refs/stash
```


```Bash
# журналы ссылок:
git reflog             # для указателя HEAD
git reflog some_branch # для ветки
git reflog stash       # для git stash


git reflog show HEAD{0}    # полная команда - git reflog
git log -g --abbrev-commit --pretty=oneline # git reflog
# eff544f HEAD@{0}: commit: migrate existing content
# bf871fd HEAD@{1}: commit: Add Git Reflog outline
git reflog show --all      # вызова полного журнала ссылок
git reflog --relative-date # относительные даты
```

# сравнение записей журнала

```Bash
# сравнение stash@{0} и some_branch@{0}
git diff stash@{0} some_branch@{0} 
name@{qualifier} # обращения к ссылке

# сравнение актуальной главной ветки 
# с главной веткой по состоянию на 1 день назад
git diff main@{0} main@{1.day.ago} 

# 1.minute.ago
# 1.hour.ago
# 1.day.ago
# yesterday
# 1.week.ago
# 1.month.ago
# 1.year.ago
# 2011-05-17.09:00:00
```

# удаление записей из журнала

```Bash
# удаляет записи журнала ссылок
git reflog expire # устаревшие или недоступные
git reflog delete # переданные
```
