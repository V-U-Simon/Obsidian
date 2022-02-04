#!/bin/bash
#1. Проверить, установлен ли пакет pillow в глобальном окружении.
#Если да — зафиксировать версию.
#Установить самую свежую версию pillow, если ранее она не была установлена.
#Сделать подтверждающий скриншот.
#
#Создать и активировать виртуальное окружение.
#Убедиться, что в нем нет пакета pillow.
#Сделать подтверждающий скриншот.
#
#Установить в виртуальное окружение pillow версии 7.1.1 (или другой, отличной от самой свежей).
#Сделать подтверждающий скриншот.
#
#Деактивировать виртуальное окружение.
#Сделать подтверждающий скриншот.
#
#Скрины нумеровать двухразрядными числами, например: «01.jpg», «02.jpg».
#Если будут проблемы с pillow - можно поработать с другим пакетом: например, requests.

# проверка наличия введенных параметров
if [ -n "$1" ]; then
  program=$1
else
  echo 'параметр не введен'
fi

# Программы уже установлена
if [[ -n $(pip3 list | grep -i $program) ]]; then
  echo "$program уже устанволена"
  echo "Фиксируем версию (обновляем requirements.txt)"
  pip3 freeze >requirements.txt && exit 0
else
  echo "$program не устанволена, ничего страшного сейчас устоновим"

  # устанавливаем программу
  pip3 install $program &&
    echo "$program устанволена успушно" \
      echo "Фиксируем версию (обновляем requirements.txt)" \
      pip3 freeze >requirements.txt
  exit 0 ||
    echo "Не удалось установить $program"
  exit 1
fi