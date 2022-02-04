"""
1. Не используя библиотеки для парсинга,
распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt

(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).

Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание:
код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

import requests
import os


def download_file(url, path_to_file):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()  # вызывает исключение в случае ошибки ответа
        # запись частями байтами
        with open(path_to_file, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
    return path_to_file


def parse(path_to_file):
    request_list = []

    with open(path_to_file, 'r') as f:
        for line in f:
            line = line.split()
            remote_addr = line[0]
            request_type = line[5].replace('"', '')
            requested_resource = line[6]

            request_list.append((remote_addr,
                                 request_type,
                                 requested_resource))

    return request_list


if __name__ == '__main__':
    url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    path_to_file = 'files/nginx_logs'

    download_file(url, path_to_file)
    for line in parse(path_to_file):
        print(line)
