# ====================================== Задача 4 ======================================
"""
Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.
"""

import utils
from utils import get_curs

# from .utils import get_curs  #todo: почему не работает
# ImportError: attempted relative import with no known parent package
# from . import utils #todo: почему не работает
# ImportError: attempted relative import with no known parent package


if __name__ == '__main__':
    print(utils.get_curs('USD'))
    print(get_curs('UsD'))
