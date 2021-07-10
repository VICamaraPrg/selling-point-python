import mysql.connector

# storemanager is the only superuser for my_store DB, So don't use root user for accessing
# (Check database\users.sql), since there is the user to use.
# storemanager has all privileges that root has, but only in my_store.
# With the ability to grant his same privileges or lower to other users.

conf = {
    'user': 'storemanager',
    'password': 'managerpassword',
    'host': 'localhost',
    'database': 'my_store'
}

db = mysql.connector.connect(**conf)
cursor = db.cursor()