---
aliases: ['локальный репозиторий', 'local repository', 'init repository', ]
created: 2022.02.13 10:01:53 pm
modified: 2022.04.28 4:31:36 pm
---

#application🛠/Git⏳/Repository

>[!cite]- Source
> - <https://ru.stackoverflow.com/questions/431520/Как-вернуться-откатиться-к-более-раннему-коммиту>
> - <https://open2web.com.ua/blog/kak-vernutsya-otkatitsya-k-bolee-rannemu-kommitu.html>
> - ⭐ [git init](https://www.atlassian.com/ru/git/tutorials/setting-up-a-repository/git-init)
> - [Какие основные задачи bare репозитория?](https://ru.stackoverflow.com/questions/542391/%d0%9a%d0%b0%d0%ba%d0%b8%d0%b5-%d0%be%d1%81%d0%bd%d0%be%d0%b2%d0%bd%d1%8b%d0%b5-%d0%b7%d0%b0%d0%b4%d0%b0%d1%87%d0%b8-bare-%d1%80%d0%b5%d0%bf%d0%be%d0%b7%d0%b8%d1%82%d0%be%d1%80%d0%b8%d1%8f)
> - [В чем разница между "git init" и "git init --bare"?](%3Chttps://fooobar.com/questions/30660/what-is-the-difference-between-git-init-and-git-init-bare%3E)

Создание чистого репозитория с возможностью последующего связывания [[git branch|локальных веток]] с удаленным репозиторием [[git branch|]] (со всеми вытекающими синхронизациями).

```shell
# cоздание нового репозитория
git init # преобразование ТЕКУЩЕГО каталога в репозиторий Git
git init <project directory> # создать новый подкаталог, будет содержать только .git

# добавление удаленного репозитория
git remote add new-remote-repo https://bitbucket.com/user/repo.git
```

# чистый репозиторий

В таком репозитории нельзя редактировать файлы и вносить изменения.

Чистый репозиторий создается для выполнения команд `git push` и `git pull`, но не для прямых коммитов.

Центральные репозитории всегда следует создавать чистыми, поскольку при отправке веток в обычный репозиторий существует риск перезаписи изменений. Просто представьте, что флаг --bare превращает репозиторий из среды разработки в хранилище.

По этой причине для рабочих процессов Git центральный репозиторий практически всегда создается чистым, а локальные репозитории разработчиков — обычными.

 >[!note]- Чистый вариант репозитория под названием `my-project` должен храниться в каталоге `my-project.git` - с постфиксом `.git`

```Bash
# пустой репозиторий Git без рабочего каталога
git init --bare <directory>

# создание репо на сервере
ssh <user>@<host> 
cd path_to_repo 
git init --bare my-project.git


ssh user@host git init --bare /path/to/repo.git
# `user` — действительное имя пользователя SSH, 
# `host` — доменный или IP-адрес сервера, 
# `/path/to/repo.git` — место, где будет храниться репозиторий. Обратите внимание, что к имени чистых репозиториев обычно добавляется расширение 
# `.git`, чтобы их можно было отличить

```
