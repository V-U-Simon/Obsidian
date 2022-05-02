---
aliases: [ ]
created: 2022.04.22 8:42:18 pm
modified: 2022.04.30 9:39:45 am
---
#application🛠/Git⏳

`git pull` - вначале забирает изменения из указанного удалённого репозитория, а затем пытается слить их с текущей веткой ([[git fetch]] и [[git merge]])

```Bash
# Исходная история
# 
#    B---C---D <- origin/main на сервере
#   /  
#  A---E---F---G   <- main 
#  ^
# origin/main на локалке

git pull origin ?main?

#    B-----C-----D  
#   /             \
#  A---E---F---G---H 
#                  ^ main(origin/main) & origin/main на сервере

git pull --rebase origin ?main?

#                E1---F1---G1  <- main 
#               /  
#  A---B---C---D   <- origin/main на сервере
#  ^
# origin/main на локалке
```
