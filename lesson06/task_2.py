"""
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов
по данным файла логов из предыдущего задания.

Примечания: спамер — это клиент, отправивший больше всех запросов;
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
    """Определяет спаммера"""
    with open(path_to_file, 'r') as f:
        ip = [line.split()[0] for line in f]
        set_ip = set(ip)

        count = map(lambda x: (ip.count(x), x), set_ip)
        return max(*count)


if __name__ == '__main__':
    url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    path_to_file = os.path.join('files', 'nginx_logs')

    download_file(url, path_to_file)
    print(parse(path_to_file))
