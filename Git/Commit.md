---
aliases: ['shoot', 'снимок' ]
created: 2022.02.13 10:01:53 pm
modified: 2022.04.29 9:51:01 am
banner: "https://wac-cdn.atlassian.com/dam/jcr:75f75cb6-a6ab-4f0b-ab29-e366914f513c/hero.svg?cdnVersion=313"
---

#application🛠/Git⏳/commit
[[ 222246.excalidraw]]

>[!cite]- Source
>
>- ⭐  [Раскрытие тайн reset](https://git-scm.com/book/ru/v2/Инструменты-Git-Раскрытие-тайн-reset)
>- ⭐ [Переписывание истории](https://www.atlassian.com/ru/git/tutorials/rewriting-history)
>- ⭐ [Сохранение изменений](https://www.atlassian.com/ru/git/tutorials/saving-changes)

**Commit** - контрольные точки на временной шкале проекта Git (запись текущего состояния в истории изменений)

Деревья git:
- **`Work directory` (WD)** - песочница
- **`index`** - Область для следующего коммита (предкоммит)  / удобно рассматривать как буфер между рабочим каталогом и историей проекта
- **`HEAD`** - Снимок последнего коммита (родитель следующего)

# на уровне коммитов

```Bash
git init                # WD <-  
git clone               # WD <-- index <-- HEAD <-- R/HEAD(all)
git pull                # WD <-- index <-- HEAD <-- R/HEAD
git fetch               # WD <-- index <-- HEAD <-- R/HEAD
git push                #                  HEAD --> R/HEAD
git reset --hard R/br   # WD <-- index <-- HEAD <-- R/br


git commit              #        index --> HEAD
git commit -a           # WD --> index --> HEAD
git revert -n HEAD      # WD <-- index <----------- HEAD~


git reset --soft  HEAD  #                  HEAD <-- HEAD~ | Перемещает HEAD и REF ветки
git reset --mixed HEAD  #        index <-- HEAD <-- HEAD~ | Перемещает HEAD и REF ветки
git reset --hard  HEAD  # WD <-- index <-- HEAD <-- HEAD~ | Перемещает HEAD и REF ветки
git checkout HEAD       # WD <-- index <-- HEAD <-- HEAD~ | Перемещает только HEAD
git revert HEAD         #                  HEAD <-- HEAD~ | Создает новый коммит


git checkout br         # WD <-- index <--  br  <-- brOLD | переключает ветку
git checkout -b new     # WD <-- index <-- brNEW <- HEAD  | создает новую ветку
git branch new          # WD <-- index <-- brNEW <- HEAD  | текущая ветка
git checkout -b new old # WD <-- index <-- brNEW <- brOLD | ветка из другого коммита
```


```Bash
git branch br_name # WD <- index <- HEAD -> br:HEAD   | Перемещает HEAD и REF ветки


REF + REF -> R:REF


br|new


```

# на уровне файлов

>[!success] Первый шаг (запись в HEAD) пропускается, т.к. указатель HEAD не может ссылаться частично на один коммит, а частично на другой коммит

```Bash
git add .                        # untracked -> WD -> index
git stage .                      # untracked -> WD -> index
git commit                       #                    index -> HEAD
git rm .                         # untracked <- WD
git restore --staged .           # untracked <- WD -- index   (untracked file)
git rm --cached .                # untracked <------- index   (untracked file)
git restore .                    #              WD <- index
git checkout .                   #              WD <- index <- HEAD
git checkout BRANCH -- file.txt  #              WD <- index <- HEAD <- HEAD~
git reset .                      #                    index <- HEAD
git reset BRANCH -- file.txt     #                    index <- HEAD <- HEAD~
```

# отслеживание файлов

```Bash
git add .               #           untracked -> tracked (index)
git restore --staged .  #           untracked <- tracked
git rm --cached .       #           untracked <- tracked 
git rm -f .             # delete <-------------- tracked
git clean -f .          # delete <- untracked
```

# [[Отмена коммита]]

 слияние

 перемещение
