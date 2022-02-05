```ad-quote
title:
## source:
- <https://losst.ru/kompilyatsiya-programm-linux>
- [Подготовка системы](https://losst.ru/kompilyatsiya-programm-linux#%D0%9F%D0%BE%D0%B4%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D0%BA%D0%B0_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B)
- [Как выполняется компиляция?](https://losst.ru/kompilyatsiya-programm-linux#%D0%9A%D0%B0%D0%BA_%D0%B2%D1%8B%D0%BF%D0%BE%D0%BB%D0%BD%D1%8F%D0%B5%D1%82%D1%81%D1%8F_%D0%BA%D0%BE%D0%BC%D0%BF%D0%B8%D0%BB%D1%8F%D1%86%D0%B8%D1%8F)
- [Компиляция программ Linux](https://losst.ru/kompilyatsiya-programm-linux#%D0%9A%D0%BE%D0%BC%D0%BF%D0%B8%D0%BB%D1%8F%D1%86%D0%B8%D1%8F_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC_Linux)
- [Получение исходников](https://losst.ru/kompilyatsiya-programm-linux#%D0%9F%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B8%D1%81%D1%85%D0%BE%D0%B4%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2)
- [Настройка configure](https://losst.ru/kompilyatsiya-programm-linux#%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0_configure)
- [Сборка программы](https://losst.ru/kompilyatsiya-programm-linux#%D0%A1%D0%B1%D0%BE%D1%80%D0%BA%D0%B0_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B)
- [Выводы](https://losst.ru/kompilyatsiya-programm-linux#%D0%92%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)
## link:

```

#app/programs/git
#act/install

---

## Установка

```shell
# linux
apt-get install git
# MacOS
brew install git
# Так же входит в состав Xcode Command Line Tools
```

## Опционально

```shell
# Опциональная установка алиасов
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'reset HEAD --'
# git unstage fileA == git reset HEAD -- fileA
git config --global alias.last 'log -1 HEAD'
git last
#  commit 66938dae3329c7aebe598c2246a8e6af90d04646
#  Author: Josh Goebel <dreamer3@example.com>
#  Date:   Tue Aug 26 19:48:51 2008 +0800
#
#  test for current head
#       Signed-off-by: Scott Chacon
# <schacon@example.com>
```
