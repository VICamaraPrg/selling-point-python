import os

from cashier_utils.user_functions import login, c
from database_utils.crud import get_product

FIRST_LOGIN = False
END_DAY = False
TICKET_OF_DAY = 1
COMMAND = ''

while not END_DAY:
    while not FIRST_LOGIN:
        if login():
            input('Check your cash (150€);')
            FIRST_LOGIN = not FIRST_LOGIN
    # TIME TO SCAN PRODUCTS!
    ticket = {}
    while True:
        scanned_product = get_product()
        if scanned_product is False:
            total = 0
            for product in ticket.keys():
                times = ticket.get(product)[0]
                price = ticket.get(product)[1]
                print('{}\t{} * \t{}€'.format(product, times, price))
                total += (price * times)
            print('------------------------------------'
                  '\nTotal to pay\t\t{}€'.format(total))
            break
        if type(scanned_product) is not None:
            name = scanned_product[0]
            price = scanned_product[1]

            if name not in ticket:
                ticket[name] = [1, price]

            else:
                ticket.get(name)[0] += 1
            c()
            print(name, price, ' *  ' + str(ticket.get(name)[0]))
