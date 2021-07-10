from database_utils.crud import validate_login, update_password, update_last_login
from database_utils.utils import generate_hash

FIRST_LOGIN = False
END_DAY = False


def login():
    id = input('Enter your worker ID:')
    login = validate_login(id)

    if login is None:
        print('That user does not exist!')
        return False
    elif login[0] == 'reset_password':
        new_pass = input('Introduce your new password:')
        update_password(id, new_pass)
        return False
    else:
        password = input('Introduce your password:')
        if login[0] == generate_hash(password, id):
            print('Logged in successfully!')
            update_last_login(id)
            return True
        else:
            print('Password does not match!')
            return False


login()
