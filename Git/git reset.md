---
aliases: [ ]
created: 2022.04.27 8:30:05 pm
modified: 2022.04.27 8:31:22 pm
---
#application🛠/Git⏳

```Bash
git reset --soft  HEAD #                HEAD <- HEAD~   | Перемещает HEAD и REF ветки
git reset --mixed HEAD #       index <- HEAD <- HEAD~   | Перемещает HEAD и REF ветки
git reset --hard  HEAD # WD <- index <- HEAD <- HEAD~   | Перемещает HEAD и REF ветки

# с файлом
git reset . # index <- HEAD
```