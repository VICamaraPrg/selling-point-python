# selling-point-python
My idea is to create a console, retro-style cashier in Python alongside with SQL database. First will do some basic features and improving them with time.

## First update, schemas and basic managing
We have the first update so far, here I cover the basics
for the application such as database creation, few products, and few functions.
<b>Mysql version: 8.0</b> 

## Things I would like to achieve:
<ul>
    <li><s>Basic product scanning</s></li>
    <li>Save tickets to DB</li>
    <li>Scan same product N times (in one command)</li>
    <li>Delete last line of product</li>
    <li>Delete a product while on the same ticket</li>
</ul>

### Things done:
<ul>
    <li>Connection to DB</li>
    <li>Basic product scanning</li>
    <li>User login</li>
</ul>

However, here's a few things to have in consideration:
First of all, create a new DB using the files in database folder in this order;
schema, users, initial_inserts.

Then you should be able to run the application (main.py).
The first time you want to log in with an user (eg: 123456)
it will ask for a reset password (4 digits), since represents it's the first time you log in.

then a message will pop up, representing you have to count the cash you have inside,
simply press enter to start scanning products.

Every product has a long reference and a short reference (up to 5 digits);
however, for being easier, just type the short reference (check initial_inserts.sql) to know some of them.

for the moment, the command to stop the ticket is '+++'. Once the ticket is stopped, you already are in another ticket.
For the next version I'd like to actually save the tickets in the DB.