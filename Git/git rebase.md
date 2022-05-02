---
aliases: [ ]
created: 2022.04.27 3:39:54 pm
modified: 2022.04.28 1:56:00 pm
---
#application🛠/Git⏳

>[!cite]- Source
>- ⭐ [git rebase](https://www.atlassian.com/ru/git/tutorials/rewriting-history/git-rebase)
>- [smartiqa](https://smartiqa.ru/courses/git/lesson-5)

# Git rebase

**git rebase (перебазирование)** - процесс перемещения последовательности коммитов к новому базовому коммиту или их объединение

**git rebase c точки зрения содержимого** - это замена одного коммита в основании ветки на другой, в результате чего создается впечатление, что ветка получила новое начало

>[!danger] ветка после rebase всегда состоит из совершенно новых коммитов

В стандартном режиме команда git rebase автоматически берет коммиты из текущей рабочей ветки и применяет их в конце переданной ветки.

```Bash
git rebase <base>

git rebase -i <base> # --interactive. |  вроде `git commit --amend` на стероидах
# p, pick   = use commit
# r, reword = use commit, but edit the commit message
# e, edit   = use commit, but stop for amending
# s, squash = use commit, but meld into previous commit
# f, fixup  = like "squash", but discard this commit's log message
# x, exec   = run command (the rest of the line) using shell
# d, drop   = remove commit

# ДО
#      o---o---o  feature  
#      |  
#  o---o---o  main  


git rebase -d # во время операции коммит будет исключен из окончательного блока объединенных коммитов.
git rebase -p # коммит останется в исходном виде. Операция не затронет сообщение и содержимое коммита. При этом сам коммит сохранится в истории веток отдельно.
git rebase -x # для каждого отмеченного коммита будет выполнен скрипт командной строки. Эта опция может быть полезной при тестировании базы кода на отдельных коммитах, поскольку с ее помощью можно выявить ошибки в ходе перебазирования.



# ДО
#        o---o---o  feature  
#       /  
#  o---o---o---o---o  main  

git branch # feature
git rebase main

# ПОСЛЕ
#                    o---o---o  feature  
#                   /  
#  o---o---o---o---o  main  
```

# расширенные возможности перебазирования

```Bash
git rebase --onto <newbase> <oldbase>
# можно передавать конкретные ссылки в качестве оснований для перебазирования



# o---o---o---o---o  main  
#      \  
#       o---o---o---o---o  featureA  
#            \  
#             o---o---o  featureB

git rebase --onto main featureA featureB

#                    o---o---o  featureB  
#                   /  
#  o---o---o---o---o  main  
#   \  
#    o---o---o---o---o  featureA

```

# отмена rebase

Необходимо передать указатель журнала ссылок  (который был перед началом `rebase`) команде `git reset` и
тем самым сбросить данные до точки перед перебазированием.

При выполнении команды сброса указатель `HEAD` переместится на коммит, в котором были добавлены изменения под названием «some WIP changes». При этом будут восстановлены другие склеенные коммиты.

```Bash
git reflog 
# 37656e1 HEAD@{0}: rebase -i (finish): returning to refs/heads/git_reflog 
# 37656e1 HEAD@{1}: rebase -i (start): checkout origin/main 
# 37656e1 HEAD@{2}: commit: some WIP changes 

git reset HEAD@{2} 
```
