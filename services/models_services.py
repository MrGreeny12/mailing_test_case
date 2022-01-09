import random
import string


def pkgen():
    '''
    Генерирует случайным образом число для primary key
    '''
    pk_detail_1 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
    pk_detail_2 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
    pk_detail_3 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
    primary_key = pk_detail_1 + pk_detail_2 + pk_detail_3

    return primary_key
