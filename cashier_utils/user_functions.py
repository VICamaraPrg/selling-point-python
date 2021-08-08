import time
import os
from database_utils.crud import validate_login, update_password, update_last_login
from database_utils.utils import generate_hash


def c():
    os.system('cls' if os.name == 'nt' else 'clear')


def login():

    id = input('Enter your worker ID:')
    login = validate_login(id)

    if login is None:
        print('That user does not exist!')
        time.sleep(2)
        return False
    elif login[0] == 'reset_password':
        new_pass = input('Introduce your new password:')
        update_password(id, new_pass)
        return False
    else:
        password = input('Introduce your password:')
        if login[0] == generate_hash(password, id):
            update_last_login(id)
            return True
        else:
            print('Password does not match!')
            time.sleep(2)
            return False
