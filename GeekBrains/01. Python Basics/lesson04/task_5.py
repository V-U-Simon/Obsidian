# ====================================== Задача 5 ======================================
"""
*(вместо 4) Доработать скрипт из предыдущего задания:
теперь он должен работать и из консоли.

Например:
> python task_4_5.py USD
75.18, 2020-09-05
"""

import sys
from utils import get_curs

exit(get_curs(sys.argv))