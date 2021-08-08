from datetime import datetime
from database_utils.db_connector import cursor, db
import hashlib


def get_product():
    product_found = False

    while not product_found:
        short_ref = input()
        if short_ref == '+++':
            return False
        sql = "SELECT p_name, price FROM product WHERE short_ref = %s"
        cursor.execute(sql, (short_ref,))
        product = cursor.fetchone()

        if product is None:
            print('This reference does not exist!')
        else:
            return product


def get_salt(id):
    sql = "SELECT password_salt FROM worker WHERE id = %s"
    cursor.execute(sql, (id,))

    return cursor.fetchone()


def update_password(id, password):
    sql = "UPDATE worker SET password_hash = %s WHERE id = %s"
    hash = hashlib.sha512(str(get_salt(id)).encode('utf-8') + str(password).encode('utf-8')).hexdigest()
    cursor.execute(sql, (hash, id))
    db.commit()

    print('Password updated successfully')


def update_last_login(id):
    sql = "UPDATE worker SET last_login = %s WHERE id = %s"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    time = datetime.now().strftime('%H:%M:%S')
    cursor.execute(sql, (timestamp, id))
    db.commit()

    print('Login time @ ' + time)


def validate_login(id):
    sql = "SELECT password_hash FROM worker WHERE id = %s"
    cursor.execute(sql, (id,))

    return cursor.fetchone()
