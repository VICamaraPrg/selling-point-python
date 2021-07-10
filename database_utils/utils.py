import random as rnd
import hashlib

from database_utils.crud import get_salt

"""
    With time, this function will be deleted, as first will check
    for all ean13 in the database, then generate them to avoid a possible duplicity.
"""


def generate_random_ean13(n):
    l = []
    for i in range(n):
        x = str(rnd.randint(100000000000, 999999999999))
        d = [int(j) for j in reversed(x)]
        c = (10 - (3 * sum(d[0::2]) + sum(d[1:2]))) % 10

        l.append(int(x) * 10 + c)
    return l


def generate_random_short_ref(n):
    l = []
    for i in range(n):
        x = rnd.randint(1001, 99999)
        l.append(x)
    return l


def generate_products(n):
    ean13 = generate_random_ean13(n)
    ref = generate_random_short_ref(n)

    for i in range(n):
        # Generate a template to fill with the product.
        print("({},{},'',,100,),".format(ean13[i], ref[i]))


def generate_hash(password, id):
    return hashlib.sha512(str(get_salt(id)).encode('utf-8') + str(password).encode('utf-8')).hexdigest()

